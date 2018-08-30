from sys import argv
import bottle
from bottle import *

bottle.debug(True)

@route("/")
def index():
    return """
    <h2> Verkefni 1. </h2>
    <p><a href="/frettir1"> Fréttagrein 1 </a></p>
    <p><a href="/frettir2"> Fréttagrein 2 </a></p>
    <p><a href="/frettir3"> Fréttagrein 3 </a></p>
    """

@route("/frettir1")
def frettagrein():
    return """
    <h2> Þrír fullorðnir menn reyndu að taka af honum vespuna </h2>
    <p> 14 ára unglingur í Breiðholti varð fyrir því í kvöld að þrír fullorðnir karlmenn réðust að honum og reyndu að ræna af honum vespu sem hann ók. Drengurinn gaf þá lýsingu á mönnunum að þeir hefðu verið um tvítugt og af erlendum uppruna, líklega frá Austur-Evrópu. </p>
    """

@route("/frettir2")
def frettagrein():
    return """
    <h2> Erum við að þvo okkur of oft um hendurnar? </h2>
    <p> Læknar, foreldrar, kennarar, leiðbeinendur og í raun allir þeir sem hjálpast að við að ala upp og kenna börnum á hreinlæti, minna þau reglulega á það að þvo sér vel um hendurnar. Handþvottur er eitthvað sem við ólumst upp við að gera reglulega og flestum finnst vera sjálfsagður hlutur. </p>
    """

@route("/frettir3")
def frettagrein():
    return """
    <h2> 9 ráð sem sálfræðingar nota þegar þeim líður illa </h2>
    <p> Sálfræðingar eru þeir sem hjálpa fólki að takast á við erfiðleika í lífinu. Hvort sem það er kvíði, þunglyndi, áráttuhegðun eða annað erfiðara sem fólk þarf að takast á við, þá er gott að geta leitað til fagmanneskju sem getur leiðbeint fólki um hvernig best sé að takast á við vandamálin. </p>
    """

#run(host="localhost", port=8060)
bottle.run(host="0.0.0.0", port=argv[1])
