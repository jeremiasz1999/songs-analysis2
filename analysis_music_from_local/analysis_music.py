import os
from pydub import AudioSegment
AudioSegment.converter = r"C:\Users\JEREMIASZ\AppData\Local\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\JEREMIASZ\AppData\Local\ffmpeg-7.1-essentials_build\bin\ffprobe.exe"

# Funkcja do dodawania pliku audio do repozytorium w pamięci
class AudioRepository:
    def __init__(self):
        self.repo = []  # Repozytorium w postaci listy

    def add_audio(self, audio):
        self.repo.append(audio)
        print("Audio added to repository.")

    def list_audios(self):
        print(f"Number of audios in repository: {len(self.repo)}")

    def modify_audio(self, index, new_audio):
        if 0 <= index < len(self.repo):
            self.repo[index] = new_audio
            print(f"Audio at index {index} modified.")
        else:
            print("Invalid index.")

# Główna funkcja programu
def main():
    # Ścieżka do pliku audio
    file_path = input("Enter the path to the local audio file: ")

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Utworzenie repozytorium
    repository = AudioRepository()

    try:
        # Załaduj lokalny plik audio
        audio = AudioSegment.from_file(file_path)
        print("Audio loaded successfully.")

        # Dodanie pliku audio do repozytorium
        repository.add_audio(audio)
        repository.list_audios()

        # Przycięcie pierwszych 10 sekund
        modified_audio = audio[:10000]  # Pierwsze 10 sekund
        repository.modify_audio(0, modified_audio)
        repository.list_audios()
    except Exception as e:
        print(f"Error processing the audio file: {e}")

if __name__ == "__main__":
    main()