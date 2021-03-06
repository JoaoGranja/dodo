% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/change_vertical_speed.R
\name{change_vertical_speed}
\alias{change_vertical_speed}
\title{Send a "change vertical speed" command}
\usage{
change_vertical_speed(aircraft_id, vertical_speed)
}
\arguments{
\item{aircraft_id}{A string aircraft identifier}

\item{vertical_speed}{The aircraft's new vertical speed in feet/min expressed as a non-negative
double or a quantity whose units can be converted to feet/min.}
}
\value{
\code{TRUE} if successful. Otherwise \code{FALSE} and an error is thrown.
}
\description{
Request an aircraft to change vertical speed.
}
\examples{
\dontrun{
change_vertical_speed("test1234", vertical_speed = 10)
}
}
