import logging
import traceback

from mopidy import core

import pykka

from .main_menu import MainMenu

logger = logging.getLogger(__name__)


class Ssd1306(pykka.ThreadingActor, core.CoreListener):

    def __init__(self, config, core):
        super(Ssd1306, self).__init__()
        self.menu = False
        self.core = core
        self.main_menu = MainMenu(self)

    def track_playback_started(self, tl_track):
        # self.speak_current_song(tl_track)
        # FIXME implement

    def playback_state_changed(self, old_state, new_state):
        # FIXME implement
        # if self.debug_gpio_simulate:
        #    if new_state == core.PlaybackState.PLAYING:
        #        self.simulator.playing_led.select()
        #    else:
        #        self.simulator.playing_led.deselect()
        #else:
        #    if new_state == core.PlaybackState.PLAYING:
        #        self.gpio_manager.set_led(True)
        #    else:
        #        self.gpio_manager.set_led(False)

    def speak_current_song(self, tl_track):
        # if tl_track is not None:
        #    artists = ""
        #    for artist in tl_track.track.artists:
        #        artists += artist.name + ","
        #    self.tts.speak_text(tl_track.track.name + ' by ' + artists)

    def playlists_loaded(self):
        # self.main_menu.elements[0].reload_playlists()
        # self.tts.speak_text("Playlists loaded")
