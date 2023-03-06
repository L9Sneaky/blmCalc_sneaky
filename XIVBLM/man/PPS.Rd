\name{PPS}
\alias{PPS}
%- Also NEED an '\alias' for EACH other topic documented here.
\title{
Potency Per Second
}
\description{
Returns expected potency per second based on Spell Speed
}
\usage{
PPS(SpellSpeed = 400, Crit = 400)
}
%- maybe also 'usage' for other objects documented here.
\arguments{
  \item{SpellSpeed}{Spell Speed Value}
  \item{Crit}{Critical Hit Rating Value (Not Used)}
}
\details{
Note: Critical Hit Rating impacts the PPS for other jobs in Final Fantasy 14. Its use in this function is future-proofing and can be ignored until Crits impact rotation.
}
\value{
Returns a double, referenced from a table, to indicate PPS values.
}
\references{
Credit to Nemekh for explicitly deriving these values.
}
\author{
Xenitan
}
\note{
Should call on a dataframe to reference, not implicitly calculate, PPS.
This table is a part of the package under the PPSTable moniker.
}

%% ~Make other sections like Warning with \section{Warning }{....} ~

\seealso{
%% ~~objects to See Also as \code{\link{help}}, ~~~
}
\examples{
}
% Add one or more standard keywords, see file 'KEYWORDS' in the
% R documentation directory (show via RShowDoc("KEYWORDS")):
% \keyword{ ~kwd1 }
% \keyword{ ~kwd2 }
% Use only one keyword per line.
% For non-standard keywords, use \concept instead of \keyword:
% \concept{ ~cpt1 }
% \concept{ ~cpt2 }
% Use only one concept per line.
