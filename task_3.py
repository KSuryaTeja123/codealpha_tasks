# Import required libraries
import numpy as np
from music21 import converter, instrument, note, chord, stream
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Activation
from tensorflow.keras.utils import to_categorical
import glob
import pickle

# Step 1: Extract Notes from MIDI Files
def load_midi_files(folder_path='midi_songs/*.mid'):
    collected_notes = []
    midi_files = glob.glob(folder_path)

    for file in midi_files:
        midi_stream = converter.parse(file)
        parts = instrument.partitionByInstrument(midi_stream)
        notes_data = parts.parts[0].recurse() if parts else midi_stream.flat.notes

        for element in notes_data:
            if isinstance(element, note.Note):
                collected_notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                collected_notes.append('.'.join(str(n) for n in element.normalOrder))
    return collected_notes

# Step 2: Prepare Training Sequences
def prepare_music_sequences(notes_collection, seq_length=100):
    unique_pitches = sorted(set(notes_collection))
    note_to_number = {note: number for number, note in enumerate(unique_pitches)}

    input_sequences = []
    output_notes = []

    for i in range(len(notes_collection) - seq_length):
        input_seq = notes_collection[i:i + seq_length]
        output_note = notes_collection[i + seq_length]
        input_sequences.append([note_to_number[n] for n in input_seq])
        output_notes.append(note_to_number[output_note])

    total_patterns = len(input_sequences)
    reshaped_input = np.reshape(input_sequences, (total_patterns, seq_length, 1))
    normalized_input = reshaped_input / float(len(unique_pitches))
    categorical_output = to_categorical(output_notes)

    return normalized_input, categorical_output, note_to_number, unique_pitches

# Step 3: Build the LSTM Model
def build_music_model(input_shape, output_size):
    model = Sequential()
    model.add(LSTM(512, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.35))
    model.add(LSTM(512))
    model.add(Dense(256))
    model.add(Dropout(0.35))
    model.add(Dense(output_size))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')
    return model

# Step 4: Generate New Music Sequences
def generate_music_sequence(model, seed_input, mapping, sequence_length=500):
    starting_point = np.random.randint(0, len(seed_input) - 1)
    pattern = seed_input[starting_point]
    generated_notes = []

    index_to_note = {value: key for key, value in mapping.items()}

    for _ in range(sequence_length):
        prediction_input = np.reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(len(mapping))

        prediction = model.predict(prediction_input, verbose=0)
        predicted_index = np.argmax(prediction)
        predicted_note = index_to_note[predicted_index]

        generated_notes.append(predicted_note)
        pattern = np.append(pattern[1:], [[predicted_index]], axis=0)

    return generated_notes

# Step 5: Convert Notes to MIDI File
def create_midi_file(notes_sequence, output_filename="generated_music.mid"):
    midi_stream = []
    offset = 0

    for note_pattern in notes_sequence:
        if '.' in note_pattern or note_pattern.isdigit():
            chord_notes = [int(n) for n in note_pattern.split('.')]
            new_chord = chord.Chord(chord_notes)
            new_chord.offset = offset
            midi_stream.append(new_chord)
        else:
            new_note = note.Note(note_pattern)
            new_note.offset = offset
            midi_stream.append(new_note)
        offset += 0.5

    music_stream = stream.Stream(midi_stream)
    music_stream.write('midi', fp=output_filename)

# Step 6: Full Pipeline
if __name__ == "__main__":
    print("Loading MIDI files...")
    music_notes = load_midi_files()

    # Save extracted notes for potential reuse
    pickle.dump(music_notes, open('music_notes_data.pkl', 'wb'))

    print("Preparing sequences...")
    input_data, output_data, note_mapping, all_notes = prepare_music_sequences(music_notes)

    print("Building model...")
    music_model = build_music_model((input_data.shape[1], input_data.shape[2]), len(all_notes))

    print("Training model (this may take some time)...")
    music_model.fit(input_data, output_data, epochs=50, batch_size=64)

    print("Generating new music...")
    new_music = generate_music_sequence(music_model, input_data, note_mapping)

    print("Saving generated music to MIDI file...")
    create_midi_file(new_music, "generated_music.mid")

    print("Music generation complete!")
