"""Provide match grabbers."""

from scctool.matchgrabber.custom import MatchGrabber as MatchGrabber
from scctool.matchgrabber.alpha import MatchGrabber as MatchGrabberAlpha
from scctool.matchgrabber.rstl import MatchGrabber as MatchGrabberRSTL

__all__ = ["MatchGrabber", "MatchGrabberAlpha", "MatchGrabberRSTL"]
