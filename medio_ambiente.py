import discord
from discord.ext import commands
import shutil
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

bad = {
    "plásticos": "Los plásticos son difíciles de descomponer y contaminan los océanos y el suelo, dañando la vida marina y los ecosistemas terrestres.",
    "pesticidas": "Los pesticidas se utilizan en la agricultura para controlar plagas, pero pueden contaminar el suelo, el agua y afectar a la biodiversidad, incluyendo insectos beneficiosos y organismos no objetivo.",
    "hidrocarburos": "Los hidrocarburos, como el petróleo y sus derivados, pueden derramarse accidentalmente y contaminar cuerpos de agua y suelos, causando daños a los ecosistemas acuáticos y terrestres.",
    "metales pesados": "Los metales pesados, como el plomo, e  n l mercurio y el cadmio, son tóxicos para los organismos vivos y pueden acumularse en el suelo y el agua, causando contaminación y daño a la vida silvestre.",
    "clorofluorocarbonos": "Los CFCs, utilizados en refrigerantes y aerosoles, pueden destruir la capa de ozono y contribuir al calentamiento global, causando daños en la atmósfera y el clima.",
    "residuos nucleares": "Los residuos nucleares, generados por la energía nuclear y otras aplicaciones, son altamente tóxicos y pueden persistir en el medio ambiente durante miles de años, representando un riesgo para la salud humana y el medio ambiente.",
    "mercurio": "El mercurio es un metal pesado que puede contaminar el agua y los alimentos. Puede causar daños neurológicos y afectar la salud humana y animal.",
    "desechos electrónicos": "Los desechos electrónicos contienen materiales tóxicos como plomo, mercurio y cadmio. Su incorrecta eliminación puede contaminar el suelo y el agua.",
    "óxidos de nitrógeno": "Los óxidos de nitrógeno son gases emitidos por vehículos, industrias y actividades agrícolas. Contribuyen a la formación de lluvia ácida y al calentamiento global.",
    "metano": "El metano es un gas de efecto invernadero que se produce por la descomposición de materia orgánica en condiciones anaeróbicas. Contribuye al calentamiento global.",
    "dióxido de azufre": "El dióxido de azufre es un gas emitido por la quema de combustibles fósiles. Puede causar lluvia ácida y afectar la calidad del aire.",
    "dianuro": "El cianuro es altamente tóxico y puede contaminar el agua y el suelo. Es utilizado en la minería de oro y puede causar daños ambientales graves si se maneja incorrectamente.",
    "plomo": "El plomo es un metal pesado utilizado en pinturas, baterías y otros productos. Su liberación al medio ambiente puede causar contaminación del suelo y el agua, afectando la salud humana y animal.",
    "monóxido de carbono": "El monóxido de carbono es un gas tóxico emitido por la combustión incompleta de combustibles fósiles. Puede causar envenenamiento y afectar la calidad del aire.",
    "amoníaco": "El amoníaco es un compuesto químico utilizado en la agricultura y la industria. Su liberación al medio ambiente puede causar contaminación del agua y afectar la salud de los ecosistemas acuáticos.",
    "hidrofluorocarbonos (HFCs)": "Los HFCs son gases utilizados como refrigerantes en sistemas de aire acondicionado y refrigeradores. Son potentes gases de efecto invernadero que contribuyen al calentamiento global.",
    "arsénico": "El arsénico es un metaloide tóxico que puede contaminar el suelo y el agua. Es liberado por actividades industriales y mineras y puede causar graves problemas de salud.",
    "fertilizantes químicos": "Los fertilizantes químicos pueden contaminar el agua y el suelo con nutrientes en exceso, causando eutrofización y dañando los ecosistemas acuáticos.",
    "aceites usados": "Los aceites usados, si se desechan incorrectamente, pueden contaminar el suelo y el agua, afectando la vida silvestre y la calidad del agua potable.",
    "partículas finas": "Las partículas finas, emitidas por vehículos, industrias y actividades de combustión, pueden afectar la calidad del aire y la salud humana, causando problemas respiratorios y cardiovasculares.",
    "plaguicidas": "Los plaguicidas son productos químicos utilizados para controlar plagas en la agricultura. Pueden contaminar el suelo, el agua y los alimentos, afectando a la biodiversidad y la salud humana.",
    "microplásticos": "Los microplásticos son pequeñas partículas de plástico que contaminan el medio ambiente, incluyendo los océanos, el suelo y el aire. Pueden ser ingeridos por la vida marina y los seres humanos, causando daños en la salud y los ecosistemas."
}

    

@bot.event 
async def on_ready():
    print(f"I´m ready! {bot.user}")

@bot.command()
async def random_th(ctx):
    th_value = random.choice(bad.values())
    await ctx.send(th_value)


@bot.command()
async def not_found(ctx, text):
    print(f"Texto recibido: {text}")
    user = ctx.author.name
    archivo = (f"{user}.txt")
    with open(archivo, "a") as file:
        file.write(text + "\n")

    carpeta = "keys_not_found"
    shutil.move(archivo, carpeta)



@bot.command()
async def bad_th(ctx, llave):
    try:
        await ctx.send(bad[llave])

    except:
        await ctx.send("No se a podido encontrar tu componente. Utiliza el comando $not_found y agrega el componente o elemento que buscaste.")


bot.run("MTIyOTE1OTg0NzE4Mjk5NTY1Nw.G8TFq6.AJsY66pFInwpO8dflfbTCLm5x45JRvRDir0QsQ")
#https://discord.com/oauth2/authorize?client_id=1229159847182995657&permissions=8&scope=bot




