class Album:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        self.songs = {}

    def add_song(self, song, duration):
        self.songs[song] = duration

    def total_runtime(self):
        total_seconds = sum(self.convert_duration(duration) for duration in self.songs.values())
        total_minutes = total_seconds // 60
        total_seconds %= 60
        return f"{total_minutes}:{total_seconds:02}"

    @staticmethod
    def convert_duration(duration):
        minutes, seconds = map(int, duration.split(':'))
        return minutes * 60 + seconds
