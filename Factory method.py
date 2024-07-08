from abc import ABC, abstractmethod
import pathlib

"""Lets you produce families of related objects without specifying their concrete classes."""

class VideoExporter(ABC):
    """Basic representation of video exporting codec"""

    @abstractmethod
    def prepare_export(self, video_data):
        """prepares video data for exporting"""

    @abstractmethod
    def do_export(self, folder:pathlib.Path):
        """Export video data to a folder"""

class LossLessVideoExporter(VideoExporter):
    """LossLess video exporter codec"""

    def prepare_export(self, video_data):
        print("Preparing lossless video data export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossledd format to {folder}")

class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with baseline profile."""

    def prepare_export(self, video_data):
        print("preparing video data for H.264 (Baseline export).")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (baseline) format to {folder}")

class H264Hi422VideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422p profile (10-bit, 4:2:2 chroma sampling)"""

    def prepare_export(self, video_data):
        print("preparing video data for H.264 (Hi422P) export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}")

class AudioExporter(ABC):
    """Basic representation of audio exporting codec"""

    @abstractmethod
    def prepare_export(self, audio_data):
        """preparing audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exporting audio data to folder"""

class AACAudioExporter(AudioExporter):
    """AAC Audio exporting codec"""


    def prepare_export(self, audio_data):
        print("preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting AAC audio data to {folder}")

class WAVAudioExporter(AudioExporter):
    """WAV Audio exporting codec"""

    def prepare_export(self, audio_data):
        print("preparing audio data for WAV export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting WAV audio data to {folder}")

class FactoryExporter(ABC):
    """Factory that represents a combination of video and audio codecs"""

    def get_video_exporter(self) -> VideoExporter:
        """ returns an instance of video exporter"""

    def get_audio_exporter(self) -> AudioExporter:
        """ returns an instance of audio exporter"""

class LowQualityExporter(FactoryExporter):
    """factory aimed to provide high speed lower quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

class HighQualityExporter(FactoryExporter):
    """factory aimed to provide high speed high quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422VideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

class MasterQualityExporter(FactoryExporter):
    """factory aimed to provide high speed master quality export"""

    def get_video_exporter(self) -> VideoExporter:
        return LossLessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()

def read_exporter() -> FactoryExporter:
    """read inputs"""
    factories = {
        "low": LowQualityExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }
    #read the desired export quality
    while True:
        export_quality = input("Enter desired output quality (low,high,master)")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}")

def main() -> None:
    """Main function"""

    fac = read_exporter()
    #create video and audio exporter
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    #prepare export
    video_exporter.prepare_export("placeholder for video data")
    audio_exporter.prepare_export("placeholder for audio data")

    #do the export
    folder = pathlib.Path("usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

if __name__ == "__main__":
    main()
