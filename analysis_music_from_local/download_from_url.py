import requests
from pydub import AudioSegment
AudioSegment.converter = r"C:\Users\JEREMIASZ\AppData\Local\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\Users\JEREMIASZ\AppData\Local\ffmpeg-7.1-essentials_build\bin\ffprobe.exe"
from io import BytesIO

# Funkcja do ściągania pliku audio
def download_audio(url):
    try:
        # Pobierz dane audio z URL
        response = requests.get(url)
        response.raise_for_status()  # Jeśli nie uda się pobrać, zgłosi wyjątek

        # Odczytaj dane audio jako BytesIO, żeby przechować je w pamięci
        audio_data = BytesIO(response.content)

        # Załaduj audio do Pydub
        audio = AudioSegment.from_file(audio_data)
        return audio
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the audio: {e}")
        return None

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
    # URL z linkiem do pliku audio
    url = input("Enter the URL of the audio file: ")

    # Utworzenie repozytorium
    repository = AudioRepository()

    # Pobieranie pliku audio z URL
    audio = download_audio(url)
    if audio:
        # Dodanie pliku audio do repozytorium
        repository.add_audio(audio)
        repository.list_audios()

        # Przykład edycji pliku audio (np. przycięcie pierwszych 10 sekund)
        modified_audio = audio[:10000]  # Pierwsze 10 sekund
        repository.modify_audio(0, modified_audio)
        repository.list_audios()

if __name__ == "__main__":
    main()