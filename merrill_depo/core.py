
# Praise for the core!


class Connector:
    """
    Holds data needed for connection to depos
    <needs specification>
    """
    ...


class Frequency:
    """
    Holds data needed for frequency interactions
    <needs specification>
    """
    ...


class Calendar:
    """
    Holds data needed for calendar interactions
    <needs specification>
    """
    ...


class Automaton:
    """
    <a structure for automated interaction, no info currently available>
    """
    ...


class DataClass:
    """
    Holds data related to
    """
    def __init__(self, frequency, calendar):

        # obligatory: frequency class
        self.frequency = frequency
        # obligatory: calendar class
        self.calendar = calendar


def connect():
    ...


def expand_frequency():
    ...


def expand_calendar():
    ...


def collapse_frequency():
    ...


def collapse_calendar():
    ...


def merge_frequency():
    ...


def merge_calendar():
    ...


def data_check_consistency():
    ...


def data_to():
    ...


def data_from():
    ...


def data_create():
    ...
