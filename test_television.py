import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_toggle():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_mute_unmute():
    tv = Television()
    tv.power()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = Muted"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_mute_when_tv_off():
    tv = Television()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up_when_tv_off():
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_down_when_tv_off():
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_up_when_tv_off():
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_down_when_tv_off():
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_volume_change_when_muted():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"
