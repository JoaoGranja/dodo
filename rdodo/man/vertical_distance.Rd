% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/vertical_distance.R
\name{vertical_distance}
\alias{vertical_distance}
\title{Vertical distance}
\usage{
vertical_distance(from_alt, to_alt)
}
\arguments{
\item{from_alt}{A vector of non-negative doubles, interpreted as an altitude in feet, or a
vector of double values with a distance unit.}

\item{to_alt}{A vector of non-negative doubles, interpreted as an altitude in feet, or a
vector of double values with a distance unit.}
}
\value{
A matrix of doubles, with units, with one row for each element in
\code{from_alt} and one column for each element in \code{to_alt}. The
\code{(i,j)}th entry is the vertical distance \code{to_alt[j] - from_alt[i]},
in metres.
}
\description{
Compute the vertical distance in metres between two altitudes. This is a
trivial helper function for \code{\link{vertical_separation}}.
}
