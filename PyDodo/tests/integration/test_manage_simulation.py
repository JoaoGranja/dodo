"""
Test load_scenario and reset_simulation functions
- return True if successful
- raise error if invalid input provided
"""

import pytest
from pydodo import (create_aircraft, reset_simulation, load_scenario,
                    pause_simulation, resume_simulation, aircraft_position)
from pydodo.utils import ping_bluebird

from requests.exceptions import HTTPError

bb_resp = ping_bluebird()



@pytest.mark.skipif(not bb_resp, reason="Can't connect to bluebird")
def test_simulation():
    """
    - Load scenario - check returns True if valid file path is provided (BlueSky)
    - Pause
    - Resume
    - Reset
    """
    aircraft_id = "TST1001"
    type = "B744"
    latitude = 0
    longitude = 0
    heading = 0
    altitude = None
    flight_level = 250
    speed = 200

    resp = reset_simulation()
    assert resp == True

    resp = create_aircraft(aircraft_id, type, latitude, longitude,
                             heading, speed, altitude, flight_level)
    assert resp == True

    pos0 = aircraft_position(aircraft_id)

    resp = pause_simulation()
    assert resp == True

    pos1 = aircraft_position(aircraft_id)
    # check that position has changed since last position call
    assert pos1.loc[aircraft_id]["latitude"] > pos0.loc[aircraft_id]["latitude"]

    pos2 = aircraft_position(aircraft_id)
    # check that position has not changed since simulation was paused
    assert pos1.loc[aircraft_id]["latitude"] == pos2.loc[aircraft_id]["latitude"]

    resp = resume_simulation()
    assert resp == True

    pos3 = aircraft_position(aircraft_id)
    # check that position has changed since simulation was resumed
    assert pos3.loc[aircraft_id]["latitude"] > pos2.loc[aircraft_id]["latitude"]

@pytest.mark.skipif(not bb_resp, reason="Can't connect to bluebird")
def test_load_scenario():
    resp = load_scenario("scenario/8.scn")
    assert resp == True

@pytest.mark.skipif(not bb_resp, reason="Can't connect to bluebird")
def test_load_empty():
    """
    Check fails if no scenario file is provided
    """
    with pytest.raises(AssertionError):
        resp = load_scenario("")

@pytest.mark.skipif(not bb_resp, reason="Can't connect to bluebird")
def test_load_invalid_file():
    """
    Check exception is raised if invalid file path is provided
    """
    with pytest.raises(HTTPError):
         resp = load_scenario("hello")