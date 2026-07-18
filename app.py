from scanner import Scanner

from processor import Processor

from report import show

from exporter import Exporter

images = Scanner().scan()

processed = Processor().process(

    images

)

show(

    processed

)

Exporter().export(

    processed

)
