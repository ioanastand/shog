from settings import (
    TARGET_WIDTH,
    TARGET_HEIGHT,
    OUTPUT_FORMAT
)


class Filters:

    def resize(self, image):

        return (

            image.width,
            image.height,

            TARGET_WIDTH,
            TARGET_HEIGHT

        )

    def convert(self, image):

        return (

            image.extension,

            OUTPUT_FORMAT

        )
