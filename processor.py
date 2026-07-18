from filters import Filters


class Processor:

    def process(
        self,
        images
    ):

        result = []

        filters = Filters()

        for image in images:

            result.append({

                "image": image,

                "resize": filters.resize(image),

                "convert": filters.convert(image)

            })

        return result
