from lsst.obs.sdss.sdssNullIsr import SdssNullIsrTask

# Read post-ISR data from fpC, fpM, asTrans, etc. files and remove overlap
config.isr.retarget(SdssNullIsrTask)

# Use the PSF determined by SDSS, without trying to fit anything better,
# because the exposures cover too small a region to do a good job of PSF fitting
config.charImage.doMeasurePsf = False

config.charImage.repair.doInterpolate = False
config.charImage.repair.doCosmicRay = False

config.charImage.background.binSize = 512
config.charImage.detection.includeThresholdMultiplier = 10.0
config.charImage.detection.background.binSize = 512
config.charImage.detection.background.binSize = 512
config.charImage.measurement.algorithms["base_CircularApertureFlux"].radii = [7.0]
config.charImage.measurement.slots.apFlux = "base_CircularApertureFlux_7_0"
config.charImage.measurement.slots.calibFlux = "base_CircularApertureFlux_7_0"

# we rarely run PSF determination on SDSS data, so we have to run our own star selector instead
config.charImage.measureApCorr.sourceSelector.name = "objectSize"

config.calibrate.detection.background.binSize = 512
config.calibrate.detection.background.binSize = 512

# use the WCS determined by SDSS (why?)
config.calibrate.astrometry.forceKnownWcs = True

# this was the default prior to DM-11521.  New default is 2000.
config.calibrate.deblend.maxFootprintSize=0

# SDSS the standard aperture correction is quoted as out to a radius of 7.43.
# According to http://www.sdss.org/dr7/algorithms/photometry.html#photo_profile this corresponds to 18.58.
# Note that 7.43/0.3961270 = 18.7566 <> 18.58. Why?
