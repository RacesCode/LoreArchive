import json
import re

# Open the JSON file
with open("messages.json", "r", encoding="utf-8") as f:
  lore = json.load(f)
# Define a regular expression to match URLs
url_regex = re.compile(r"(https?://\S+|www\.\S+)")

# Define a regular expression to match @ tags
at_regex = re.compile(r"@(\S+)")

# define list of message ids from prior to the ";" identifier being used to be pulled
oldLore = [
    '799303733728641044',
'800830943974653972',
'804549060076896287',
'805278877051387945',
'805723305122070539',
'811820701659955232',
'812259899719417927',
'812574629055037451',
'814059483457388545',
'816987998909628426',
'818915589263196171',
'841385692508454952',
'843543354524434442',
'850150121986457600',
'850509178199212042',
'852324272092610604',
'857724101790400522',
'858465664386072626',
'859556997758189598',
'859924599047192629',
'860639640460984331',
'862458552642961438',
'864271679588663336',
'883795725090160641',
'884153297588613131',
'884885271890505730',
'885972796608495686',
'888505609245327400',
'888876003995287643',
'889236615531216896',
'889955411963305984',
'890688295120535663',
'891413035686703105',
'893589096142872587',
'895074127763877929',
'895393446481760328',
'895766909289635861',
'896497441543708683',
'897945391415328778',
'898678429765996554',
'901210259308281946',
'901584756075008000',
'910286983656538142',
'916462047930232873',
'917194166004490300',
'917567571119714304',
'917929057348358154',
'918296050521997392',
'918650232106000395',
'920079648757526598',
'920442311572357171',
'921535864994156544',
'921909830304792576',
'923726577374740500',
'924825599690817546',
'929176405391069214',
'933876140492328960',
'938584003647242251',
'939675966467371068',
'942198782467121152',
'942554448327237702',
'943658162941222912',
'944712499805159495',
'946544921425350706',
'946893911668957194',
'947238746389115000',
'952717604148084766',
'953786752106119258',
'954869929084063775',
'959217645377454171',
'959586302406328370',
'961392790036705310',
'962120057935245344',
'964295226111971348',
'964668018120605798',
'967187572029800528',
'967187599980642325',
'967929267176472606',
'967929280698916924',
'972633010103005204',
'972633020983025684',
'974079286396985345',
'974798264148824144',
'975158095724576808',
'975524816251666482',
'979873857353678849',
'981330747245867038',
'981330757882634262',
'981692799768485969',
'981692837550772234',
'981692892202553384',
'982044235882713159',
'982768328491794493',
'982768353431134309',
'982768391586738247',
'983857619808682054',
'983857645557518367',
'984581348813582456',
'987489633006944256',
'987845637309607987',
'990380264716910592',
'999807238199849041',
'100162830514285376',
'100200188637269207',
'100235545972389491',
'100271197012389072',
'100307225750719699',
'100451489064133019',
'100524273589839883',
'100670627233216514',
'100777396808371405',
'100920822562896696',
'101068522474256793',
'101176973182239953',
'101248445790054414',
'101320162867072215',
'101355998090284241',
'101428118607338708',
'101465796138317827',
'101538046222873804',
'101574281765979750',
'101683446602872022',
'101719633272688244',
'101936668549868749',
'101973562831903545',
'102045920681972125',
'102081814750010578',
'102190348078653455',
'102229473119726388',
'102300459314106368',
'102300462633059533',
'102336209919753019',
'102371965072860775',
'102443693523575195',
'102480975982992183',
'102552400065227576',
'102624559313323628',
'102806646499077332',
'103712517305427563',
'103786127259258471',
'104075437919358976',
'104113707243562619',
'104221831218202627',
'104367166070589032',
'104586327247106871',
'104799394691312030',
'104799399771032791',
'105055175824350413',
'106369228774336927',
'106442442566926338',
'106590331468173315',
'106652940151425028',
'106687530135689625',
'106795678052674769',
'106898821410010321',
'106945496387028590',
'107019856529878631',
'107050383479696598',
'107122482165817352',
'107122487847839338',
'107302335977383944',
'107375091157225079',
'107487745025482754',
'107630791825477633',
'107699894469920783',
'107770375220049925',
'107770379793098756'
          ]

# define list of names to tag
names = ['Aarand Vullan'
, 'Aarand'
, 'Khri Ettur'
, 'Khri'
, 'Roln'
, 'Armedius'
, 'Undel, Exiled King'
, 'Kyr'
, 'Ryn'
, 'Petyl'
, 'Mirh'
, 'Baz'
, 'H\'rol'
, 'Eri'
, 'Captain'
, 'Don'
, 'Gull'
, 'Xeno'
, 'Pavel'
, 'Ki'
, 'Cel'
, 'Rallyn'
, 'Irie'
, 'Egol'
, 'Tal'
, 'Jun'
, 'Barnib'
, 'Linim'
, 'Jov The God of Chance'
, 'Leon The Scholar'
, 'Riv'
, 'Ganren'
, 'King Tem'
, 'Kedrel'
, 'Fin'
, 'Y\'lyat'
, 'Vuli'
, 'Penm'
, 'Teagel '
, 'Nim'
, 'Sellira'
, 'Bell '
, 'Lez'
, 'Orel'
, 'Wendel'
, 'Ven Rallet'
, 'Cera Forethrell'
, 'Rib'
, 'Pipe'
, 'Judge Forethrell'
, 'Perin'
, 'Nym Blas'
, 'Wev'
, 'Visia'
, 'Jack'
, 'Samson'
, 'Gren'
, 'Rel'
, 'Fellren'
, 'Brint'
, 'Seers'
, 'Silvena'
        ]

# define list of place names to tag
places = [
     'Windfall'
, 'Wintrell'
, 'Fifteen'
, 'Eden'
, 'Outer Edge'
, 'Ysimji'
, 'Multiverse'
, 'Universe'
, 'Mivera'
, 'Veil'
, 'Pulse'
, 'Divide'
, 'Colorless Grove'
, 'Aether'
, 'Gentig'
, 'Aurium'
, 'Elrin'
]

# Define a function to process the content of a message
def process_content(content):
  # Remove URLs
  content = url_regex.sub("", content)
  
  # Remove @ tags
  content = at_regex.sub("", content)
  
  # Convert \n to new line
  content = content.replace("\\n", "\n")

  # Remove ; identifier
  content = content.replace(";","")

  # search for names and add [[]] tags
  for name in names:
    pattern = r'\b{}\b'.format(name)
    content = re.sub(pattern, f'[[{name}]]', content)
    
    return content

# Loop through the messages and create .md files for the ones that meet the criteria
count = 1
for messages in lore["messages"]:
  content = messages["content"]
  if ";" in content or messages["id"] in oldLore:
    filename = str(count) + ".md"
    with open(filename, "w", encoding="utf-8") as f:
      timestamp = messages["timestamp"][:10]
      content = process_content(content)
      f.write(f"**[{timestamp}]**\n\n**{content}**")
    count += 1
