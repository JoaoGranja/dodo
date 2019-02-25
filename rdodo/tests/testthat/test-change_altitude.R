require(testthat)
context("change_altitude function")

skip_if_not(found_bluebird(), message = "BlueBird not found: tests skipped.")

# Reset the simulation to ensure no aircraft exist initially.
reset_simulation()

test_that("the change_altitude function works", {

  aircraft_id <- "test-change-altitude"
  type <- "B744"
  latitude <- 0
  longitude <- 0
  heading <- 0
  flight_level <- 250
  speed <- 200

  # Create an aircraft.
  expect_true(create_aircraft(aircraft_id = aircraft_id,
                              type = type,
                              latitude = latitude,
                              longitude = longitude,
                              heading = heading,
                              flight_level = flight_level,
                              speed = speed))

  # TODO: replace hard-coded string "altitude" with config parameter (see also
  # other list elements in aircraft_position):

  # Check the altitude.
  position <- aircraft_position(aircraft_id)
  expect_identical(object = position[["altitude"]], expected = flight_level * 100)

  # Give the command to ascend.
  new_flight_level <- 450
  expect_true(change_altitude(aircraft_id = aircraft_id,
                              flight_level = new_flight_level))

  # Check that the new altitude exceeds the original one.
  new_position <- aircraft_position(aircraft_id)
  expect_true(new_position[["altitude"]] > flight_level * 100)
})