# Disease name
# Symptoms
# Causes
# Cure

# more information
# Doctors

import sqlite3


def add_many(List):
    conn = sqlite3.connect('disease.db')
    c = conn.cursor()
    for item in List:
        c.execute("INSERT INTO diseases VALUES (?,?,?,?)", item)
    conn.commit()
    conn.close()


stuff = [
    ("Acidity",
     "",
     """Common Causes:
     Consumption of alcohol
     Highly spicy foodstuffs
     Non-vegetarian diets
     Non-Steroidal Anti-Inflammatory Drugs (NSAID's)""",
     """Home Remedies:
     After all three meals, take a small piece of jaggery and keep it in your mouth and suck. Voilá no more acidity.
     Boil one cup of water. To this add 1 tsp of aniseed (Saunf). Cover and leave overnight. Strain the water in the morning, add 1 tsp of honey. When this is taken 3 times a day it prevents acidity.
     Powder one clove and one cardamom; use the powder as a mouth freshener after every meal. No more acidity and no more bad breath.""",
     ),
    ("Acne",
     "",
     """Common causes:
     Secretion of an excessive amount of oil in the skin
     Hormonal changes during puberty
     Accumulation of oily secretions on the skin surface
     Blockage of the external pores in the skin
     Stress""",
     """Home Remedies:
     Fresh lime juice may be dabbed on pimples and blackheads.
     Make a paste of fresh, young curry leaves apply and keep on overnight wash with warm water in the morning. Helps wrinkles to fade away gradually.
     For dry skin rub a piece of sandalwood on a smooth stone with a few drops of raw milk. Apply the paste procured on affected areas. Keep on for 1 hour. Gently wash.""",
     ),
    ("Age_Spots",
     "",
     """Causes:
     Overexposure of skin to sun rays causes increased production of melanin to protect the inner layers of skin from harmful UV rays.
     Prolonged use of electronic tanning lamps and tanning beds can also cause skin darkening. Aging, chronic illness and poor nutrition are also contributing factors for age spots.""",
     """Home Remedies:
     Lemon Juice: Lemon juice is one of the best remedies to reduce age spots.
     Aloe Vera: Aloe Vera juice or gel is another good treatment for age spots. It helps clear marks and diminishes dark spots effectively.""",
     ),
    ("""Alcoholism""",
     """""",
     """Common Causes:
     Depression
     Schizophrenia
     Established behavior patterns
     Environment
     Damaged relationships
     """,
     """Home Remedies:
     First and foremost, the person should be willing to give up alcohol. Sadly, but very true that the only way to do it is, to make a clean break.
     Eating as many apples as possible at regular intervals can, reduce your craving for alcohol. They also help to clear the toxins from the system.
     Grapes contain a pure form of alcohol. A person wanting to give up this habit should have a meal of grapes every 4-5 hours, for a month at least.
     """
     ),
    ("""Anemia""",
     """""",
     """Common Causes:
     Bleeding (hemorrhage)
     Iron deficiency
     Body inability to produce sufficient red blood cells
     Hemolysis
     Pregnancy
     Menstruation
     Piles
     Hiatus hernia
     Hookworm infestation""",
     """Home Remedies:
     1 Cup beetroot juice, 1 cup of apple juice, mixed with either sugar or honey once a day.
     Consume a ripe banana with 1 tbsp of honey 2 times a day.
     Soak 10 currants overnight. Remove seeds and have for 3-4 weeks early in the morning.
     """),
    ("""Anorexia""",
     """""",
     """Common Causes:
     Dieting
     Emotional problems
     Genes
     Imbalance of chemicals in the brain
     """,
     """Home Remedies:
     Boil 2-3 cloves of garlic in 1 cup of water. Strain. Add the juice of ½ a lime to this and drink 2 times a day, for a week.
     Make a paste of fresh Ginger. Add a pinch of salt and a drop of lime juice to ½ a tspn of the paste. Eat this 2 times a day for 1 week.
     Eat at least 1 Apple a day."""),
    ("""Appendicitis""",
     """Symptoms:
     Sharp pain in lower right abdomen Coughing or sneezing increases abdominal pain.
     Inability to pass gas (break wind, fart)
     Painful urination Severe cramps
     Loss of appetite
     Constipation""",
     """""",
     """Home Remedies:
     Drinking plenty of water throughout the day is essential for a healthy appendix.
     Prepare a cup of ginseng tea and have it twice daily, as it helps in curing the pain and inflammation of the appendix.
     Green gram is an effective remedy for treating appendicitis. Take 1 tablespoon of green gram soaked in water thrice daily.
     Consume equal quantity of honey and lemon juice to prevent indigestion during appendicitis.
     Buttermilk is very effective in preventing the bacterial growth in the appendix. Consume a liter of buttermilk daily."""
     ),
    ("""Asthma""",
     """""",
     """Common Causes:
     Allergy to pollen, dust particles
     Ait pollution
     Respiratory infections
     Sulfites in food""",
     """Home Remedies:
     Mix 1 tsp of honey with ½ tsp of cinnamon powder. Consume the mixture just before sleeping to treat asthma.
     Boil 8-10 cloves of garlic in ½ cup of milk. Have it at night, as it is good for the early stages of asthma.
     Figs are good for draining phlegm. Wash 3-4 dry figs with water. Soak in 1 cup of water. Eat these on an empty stomach and drink the water that the figs were soaked in also. Do not eat anything else for an hour at least. Do this for 2 months"""
     ),
    ("""Back_Pain""",
     """""",
     """Common Causes:
     Slipped disc and fracture in bones are the most common injuries resulting in back pain.
     Over Straining of Back Muscles
     Arthritis
     Skeletal Irregularities""",
     """Home Remedies:
     Core Strengthening Exercises
     Body Weight Management
     Boost Calcium Intake
     Sleep Properly"""),
    ("""Bad_Breath""",
     """""",
     """Common Causes:
     Bad dental hygiene is one of the main reasons of bad breath. When food particles are stuck between tooth cavities they can smell bad.
     Gum disease-gingivitis- is also a major cause and a dentist should be consulted at the earliest.
     Constipation and an upset stomach also cause bad breath.""",
     """Home Remedies:
     Brush teeth two to three times a day.
     Mix 1 teaspoon of salt to a glass of water and gargle with this three times a day.
     Mix ½ teaspoon salt to 1 teaspoon of mustard oil and massage the gums with this, it tightens the gums and prevents gum disease and keep away bad breath."""
     ),
    ("""Bedwetting""",
     """""",
     """Common Causes:
     Inability to wake up from sleep
     Overactive bladder
     Constipation
     Genetic factors""",
     """Home Remedies:
     Urinate twice before going to bed
     Reduce liquid consumption in the evening (deprivation)""",
     ),
    ("""Body_Odor""",
     """""",
     """Common Causes:
     Moist and warm environments aid bacterial and fungal growth, providing them perfect temperatures to multiply.
     Stress, anxiety, menstruation in women and anger cause increased sweating and therefore more odor.""",
     """Home Remedies:
     Bathing and proper cleaning of body is necessary to avoid growth of bad smelling microorganisms.
     Vinegar lowers body pH that stops bacteria from multiplying as they cannot survive in acidic environment
     A mix of 4-5 essential oils can act as homemade deodorant that leave your body fragrant, sweat free and fresh."""
     ),
    ("""BP-High""",
     """""",
     """Common Causes:
     Obesity
     Abnormal blood vessels
     Genetic factors
     Excessive alcohol""",
     """Home Remedies:
     Carrots, Spinach and Parsley to Keep Blood Pressure Under Control
     Indian gooseberry (Amla) is an effective home remedy for high blood pressure.
     Ginger Juice with Honey and Cumin Powder for High Blood Pressure"""
     ),
    ("""BP-Low""",
     """""",
     """Common Causes:
     Dehydration (due to sweating and/or diarrhea)
     Medications (for high BP or other treatments
     Pregnancy
     Fainting""",
     """Home Remedies:
     Soak 32 small raisins in a ceramic bowl full of water over night. Chew them one by one first thing in the morning. Chew well and drink the water also.
     Soak 7 almonds in water over night. Peel them and grind to a smooth paste. Add in a glass of milk and boil. Drink warm.
     Crush 10-15 holy basil leaves (tulsi) and strain through a clean muslin cloth. Mix with 1 tsp honey. Have it the first thing in the morning."""
     ),
    ("""Tooth_Ache""",
     """""",
     """Common Causes:
     Tooth pain occurs due to various causes including tooth decay or cavities, abscesses, broken or damaged teeth, sinus infections and gum disease.
     In a broken tooth, the outer hard tissues are cracked and movement such as chewing can lead to the movement of the pieces which irritates the pulp.
     """,
     """Home Remedies:
     Lime is also an effective home remedy for toothache and promotes the general health of the teeth
     The antiseptic properties of clove oil have made it one of the most popular home remedies for tooth infection pain. It numbs the affected teeth and gums thus relieving the pain.
     Babool tree bark is an excellent Ayurvedic herbal home remedy which can take care of the pain. It is also used to stop any bleeding in the tooth."""
     ),
    ("""Bronchitis""",
     """Symptoms:
     Persistent cough, chest pains, tiredness, fevers, difficulty in breathing and mucus production.
     Presence of Blood in mucus.""",
     """Common causes:
     Acute bronchitis is a viral infection. At times it is also caused by a bacterial infection though it’s not very common.
     Cigarette smoking is one of the chief causes of chronic bronchitis.
     Inhalation of polluted air due to the presence of toxic gases, industrial fumes or sulfur dioxide can also cause bronchitis.""",
     """Home Remedies:
     Inhalation of steam helps clear phlegm and mucus from the bronchial tubes and lungs.
     Ginger contains anti-inflammatory properties, which help clear mucus from lungs.
     Honey is packed with mineral and enzymes that help clear out infections from the body and reduce inflammations."""
     ),
    ("""Burns""",
     """Prevention:
     Store gasoline, lighter fluid and other highly flammable materials in a safe and secure container.
     Do not smoke in bed.
     Keep a fire extinguisher in an easily accessible spot in your kitchen.""",
     """Dos and Don'ts:
     Don’t use ice or an ice pack for burns; instead, hold it under cold running water for 5 to 10 minutes. If this is not possible, immerse the burn in cool water or use a cold compress.
     Don’t use butter, grease or any type of oil on the burn; instead, apply a first aid cream for burns to the area
     Don’t use cotton or any fluffy dressing to cover the burn; instead, lightly bind the area with a sterile gauze bandage.""",
     """Home Remedies:
     Apply a thin layer of honey to a strip of gauze and use this to bandage your burn.
     Aloe vera is another popular herb that is often touted as the cure to all problems.
     Refrigerate a couple of used tea bags and then place them over the burn. Use a clean strip of gauze to hold them in place. This remedy will reduce the pain and inflammation."""
     ),
    ("""Chapped_Lips""",
     """""",
     """Common Causes:
     Dehydration
     Licking Lips
     Allergens""",
     """Home Remedies:
     Papaya acts as a natural exfoliant. Apply mashed, ripe papaya to the lips and rinse off after 10 minutes.
     Gently rub a small slice of cucumber across your dry lips and leave it for 15- 20 minutes and then wash lips with water.
     Topical application of aloe vera gel, olive oil, mustard oil or coconut oil multiple times in a day function as natural moisturizers.""",
     ),
    ("""Chest_Congestion""",
     """""",
     """Common Causes:
     Chest congestion due to bronchitis may be caused due to many factors such as infection, or irritation from fumes, dust or pollutants in the environment
     There are various risk factors, which may lead to chest congestion such as smoking, reduced immunity or pre-existing condition of asthma.""",
     """Home Remedies:
     Anise has expectorant and has antibacterial properties, and aids in soothing the throat. Therefore, it is an important constituent of several cough syrups and lozenges.
     Camphor is an essential ingredient in various products that are applied locally and is available as an over-the-counter medicine for chest congestion. 
     An important ingredient of many cold rubs and balms, eucalyptus is another great herbal remedy for chest congestion.""",
     ),
    ("""Chickenpox""",
     """""",
     """Common causes:
     Herpes Zoster Virus
     Poor immune system
     Contact with broken Chickenpox blisters""",
     """Home Remedies:
     Mix ½ tsp of baking soda in 1 glass of water. Sponge the person with this solution. When soda dries on the skin, it controls the itchiness and irritation.
     Pure honey smeared on the scabs helps in clearing up scars.
     Application of vitamin E oil helps and has a healing effect. The scars fade away very quickly.""",
     ),
    ("""Cold""",
     """""",
     """Common Causes:
     Viruses (especially, rhinoviruses and coronaviruses)
     Allergic disorders
     Person to person (through cough, sneezing or hand contact)""",
     """Home Remedies
     Lots of rest - Resting conserves energy in the body. Infants, when allowed to sleep well, are able to activate their immune system to tackle the infection.
     Drink lots of fluids - Warm milk, water, diluted juice
     A saline solution can be sprayed or used as drops in the nose to clear out the mucus in the nasal passages, and thus relieve congestion.""",
     ),
    ("""Constipation""",
     """""",
     """Common Causes:
     Low fiber diet, Low fluid intake, Lack of exercise,
     Weak bowel muscles, Hemorrhoids,
     Excessive intake of calcium or iron, Irritable bowel syndrome""",
     """Home Remedies:
     Fruit juices such as those of prune, pear or apple help soften the stool. Do not give prune juice to infants, even if it is watered down; it serves as an irritant. 
     High fiber foods can help ease the passage of stool and relieve constipation. 
     Adequate fluids are necessary to resolve constipation.""",
     ),
    ("""Corns""",
     """""",
     """Common Causes:
     Increased skin pressure
     Deformed toes
     Rubbing of the toe against the stitch inside the shoe""",
     """Home Remedies
     Chalk, powdered and made into a paste by adding water, is very effective when applied on corn at bedtime.
     Liquorice powdered and mixed with either mustard or sesame oil (Gingili oil) to make a paste should be applied on the corns 2-3 times a day.
     Pumice stones are useful for treating corns. Rub this pumice stone on wet and moist feet after having a warm bath""",
     ),
    ("""Cough""",
     """""",
     """Common Causes:
     Viral Infection, Flu, Smoking
     Asthma, Tuberculosis, clot in lung, Pneumonia""",
     """Home Remedies:
     Take 3 peppercorns with a pinch of black cumin seeds (shah jeera) and a pinch of salt.
     3-5 drops of clove oil mixed with a clove of crushed garlic and ½ tsp honey helps soothe the throat
     In a cup of boiling water add 1 tsp turmeric powder and 1 tsp carom seeds (ajwain). Boil till half. Add 1 tsp of honey and have 2 times a day.""",
     ),
    ("""Dandruff""",
     """""",
     """Common Causes:
     Yeast sensitivity
     Dry Skin
     Seborrheic Dermatitis""",
     """Home Remedies:
     It is believed that brushing your hair right after shampoo can help curb dandruff problems.
     Coconut oil is one of the best and widely used home remedies to cure dandruff.
     Fenugreek seeds can be a good natural anit-dandruff agent.""",
     ),
    ("""Depression""",
     """""",
     """Common Causes:
     Change in brain structures or brain functions
     Pessimistic attitude
     Stress, Hormonal disorders, Financial problems""",
     """Home Remedies:
     An apple taken with milk and honey is highly effective in uplifting mood.
     Add a handful of fresh Rose petals to a cup a boiling water. Add sugar and drink as and when a feeling of depression sets in.""",
     ),
    ("""Dermatitis""",
     """Symptoms:
     Red and raised blisters
     Rashes
     Skin contains fluid, which oozes out id blisters break
     Ulceration""",
     """Common Types:
     Atopic Dermatitis
     Contact Dermatitis
     Stasis Dermatitis
     Discoid Eczema""",
     """Home Remedies:
     Drink Adequate water
     Aloe Vera can be consumed as well as applied topically.
     Turmeric is recommended for skin conditions for its anti-inflammatory and anit-bacterial properties""",
     ),
    ("""Diabetes""",
     """""",
     """Common Causes:
     Insulin deficiency
     High cholesterol
     Rarely due to pacreatitis""",
     """Home Remedies:
     Basil leaves are packed with antioxidants that relieve oxidative stess and have essential oils that help in lowering blood sugar levels in the body.
     Indian Blackberry is considered to be an effective medicine for treating diabetes.
     Drink a cup of green tea on an empty stomach daily in the morning before your breakfast""",
     ),
    ("""Diarrhoea""",
     """""",
     """Common causes:
     Infection caused by virus or bacteria.
     Infected foods.
     Drinking too much alcohol.
     Side effects from some medicines.""",
     """Home Remedies:
     Mash a ripe banana. Mix with 1 tsp of tamarind pulp and a pinch of salt. Take twice a day.
     A tsp of date paste mixed with 1 tsp honey. To be taken 4-5 times a day.
     Have 1 cup of fresh Pomegranate juice 3-4 times a day.""",
     ),
    ("""Dry_Skin""",
     """""",
     """Common Causes:
     Weather
     Bathing frequently
     Hypothyroidism
     High Blood Glucose""",
     """Home Remedies:
     Use of fragrance-free oils such as petroleum jelly, mineral oil provide protection from dry skin temporarily.
     A daily does of 100mg Vitamin B-Complex.
     Aloe Vera gel""",
     ),
    ("""Earache""",
     """""",
     """Common Causes:
     Blockage in ear tube
     Damage to ear drum
     Sinusitis
     Pharyngitis
     """,
     """Home Remedies:
     Grind a few basil leaves and extract some juice. Apply 2 drop inside the ear.
     Drip 2 or 3 drops of warm mustard oil into the infected ear and allow it to remain there.
     Include foods in your diet that are rich in Vitamin C such lemons, oranges, guavas, strawberries and papayas to reduce the earache.""",
     ),
    ("""Eczema""",
     """""",
     """Common Causes:
     Dust mites and pollen.
     Soaps or detergents.
     Specific allergies to foods.""",
     """Home Remedies:
     Coconut oil can be used as a natural moisturizer.
     Nutmeg against a smooth stone with a few drops of water. Make a smooth paste. Apply.
     Bathing plays an important role in eczema treatment, as it helps moisturize the skin.""",
     ),
    ("""Fatigue""",
     """Types of Fatigue:
     Central fatigue: The rate of muscle activation controlled by the central nervous system is impaired.
     Peripheral fatigue: The rate of muscle activation controlled by other peripheral mechanisms is impaired.""",
     """Common Causes:
     Abnormal functioning of the immune system.
     Lack of sleep, irregular work shifts, pregnancy, sleep apnea, Alcohol or drug abuse.
     Medications such as anti-histamines, anti-depressants, sedatives""",
     """Home Remedies:
     Drink lot of water. One must drink at least 8 glasses of water a day. It is not sufficient to wait till you are thirsty to drink water.
     Have magnesium, vitamin E, vitamin C, and calcium supplements
     In order to deal with stress and anxiety, techniques such as deep breathing, meditation, and yoga are recommended.""",
     ),
    ("""Fever""",
     """Symptoms:
     Some symptoms during a fever are headache, sweating, shivering, burning eyes, muscle ache, dehydration, loss of appetite, body pain and weakness.
     A high fever in the range of 103 °F to 106 °F can also cause symptoms such as irritability, hallucinations and convulsions.""",
     """Common Causes:
     Sunburn, cold & flu, infection in the ear or throat can cause fever.
     Fever can also be present due to malaria, typhoid or hypothermia.
     Fever may be present during infection of the urinary tract, meningitis, measles, chickenpox, typhus, hyperthyroidism and pneumonia.
     Essentially there may be any number of reasons that can cause high body temperature. On certain occasions, the cause of fever is difficult to determine""",
     """Home Remedies:
     Ginger tea reduces inflammations and infections, thereby, reducing the fever.
     Capsaicin found in cayenne pepper induces sweating and improves blood circulation. This is why the use of cayenne pepper is one of the most useful home remedies for fever.
     Drinking lemon juice in lukewarm water can ward off the fever.""",
     ),
    ("""Fever blisters""",
     """home remedies:
     Apply petroleum jelly to the skin.
     Apply cold compress on the affected area.
     Avoid eating nuts and chocolate.""",
    ),
    ("""Eczema""",
     """""",
     """Common Causes:
     Dust mites and pollen.
     Soaps or detergents.
     Specific allergies to foods.""",
     """Home Remedies:
     Coconut oil can be used as a natural moisturizer.
     Nutmeg against a smooth stone with a few drops of water. Make a smooth paste. Apply.
     Bathing plays an important role in eczema treatment, as it helps moisturize the skin.""",
     ),
    ("""Lice""",
     """""",
     """Common Causes:
     Lice spread through close head-to-head contact
     Sharing of combs, brushes etc.""",
     """Home Remedies:
     Make a mixture with 1 teaspoon lime juice and 1 teaspoon garlic paste. 
     Apply on scalp. Leave for half hour and wash.
     Salt can help remove head lice through desiccation. Mix one-quarter cup of salt and one-quarter cup of vinegar thoroughly.
     Gently spray the mixture onto your 
     hair till it becomes slightly wet. Use a shower cap to cover your head, leave it for about two hours. Then wash and shampoo your hair.""",
     ),
    ("""Low_Back_Pain""",
     """""",
     """Common Causes:
     Wrong posture while sitting, standing, 
     walking or lifting heavy objects is the most 
     common cause of all back pains. Other causes 
     of back pain include slipped disc, sciatica, 
     whiplash, frozen shoulder and ankylosing spondylitis.""",
     """Home Remedies:
     Soothe the Pain with Cold or Hot Packs
     Get Some Sleep in a Comfortable Mattress
     Correct Your Posture – Sitting, Standing and Walking
     Be on the Move.""",
     ),
    ("""Malaria""",
     """""",
     """Common Causes:
     Plasmodium parasites (cause malaria)
     Anopheles mosquitoes (spread malaria)
     Climatic conditions
     Travelers
     Migrants.""",
     """Home Remedies:
     No Home remedies treatment by doctors expected.""",
     ),
    ("""Measles""",
     """""",
     """Common Causes:
     Personal contact
     Droplets from coughs and sneezes
     Immunodeficiency due to HIV/AIDS
     Malnutrition
     Vitamin A deficiency.""",
     """Home Remedies:
     Fresh Orange juice had 2 times is good
     Barley water should be taken 2-3 times.
     Lemonade should be taken often.""",
     ),
    ("""Menstrual_Cramps""",
     """""",
     """Common Causes:
     Primary dysmenorrhea or menstrual cramps 
     usually affect young girls and are caused due to contractions of the 
     uterus that occur in response to prostaglandin, a hormone-like substance that works to stimulate contractions necessary for shedding the uterine lining.""",
     """Home Remedies:
     Regular Exercise
     Use Hot Water Bottle
     Drink Water
     Yoga.""",
     ),
    ("""Mouth_ulcer""",
     """""",
     """Common Causes:
     Nutritional deficiencies such as iron, vitamins, especially B12 and C
     Poor dental hygiene
     Food allergies
     Stress
     Infections, particularly herpes simplex
     Biting the cheek.""",
     """Home Remedies:
     grate some fresh coconut. 
     Extract the milk and gargle with this 3-4 times a day.
     Keep 1 glass of chilled water and 
     1 glass of hot water ready at hand. 
     Gargle alternately with hot and cold water.""",
     ),
    ("""Mumps""",
     """""",
     """Common Causes:
     Paramyxovirus
     Droplets from coughs and sneezes
     Lack of immunization.""",
     """Home Remedies:
     Make a paste made with dry ginger 
     powder and water and apply it on the
     visibly swollen parts.
     Aloe Vera is an excellent remedy for treating mumps. Peel off a fresh piece of Aloe Vera leaf and rub the gel 
     on the affected area to relieve from swelling and pain.""",
     ),
    ("""Neck_Pain""",
     """""",
     """Common Causes:
     Muscle strain
     Sitting in an improper posture,
     sleeping in the wrong position.""",
     """Home Remedies:
     Cold or Warm Packs
     Transcutaneous Electrical Nerve Stimulation.""",
     ),
    ("""Nosebleed""",
     """""",
     """Common Causes:
     Nose picking
     Nose injury
     Cold or flu
     Inserting small objects
     Allergies.""",
     """Home Remedies:
     Dab a cotton ball in apple cider vinegar and place in your nostril. 
     This helps in reducing the flow of blood from your nose.
     Apply an ice pack or cold compress across the
     bridge of your nose for at least 5 to 10 minutes.""",
     ),
    ("""Obesity""",
     """""",
     """Common Causes:
     Lifestyle
     Excess calorie intake
     Quality of diet (too much of fatty foods)
     Spacing of meals (eating very often)
     Hormones
     Metabolism.""",
     """Home Remedies:
     Make a mixture of 1 teaspoon of honey and lemon juice in a glass of warm water,
     mix well and have this mixture daily in the morning.
     Vegetables such as tomatoes, carrots and dark green leafy vegetables are low-calorie foods that are good for your health. Therefore, include some vegetables salad and fruits in your daily
     diet to keep you full and satisfied throughout the day.
     """,
     ),
    ("""Osteoporosis""",
     """""",
     """Common Causes:
     Age
     Hormone levels
     Optimal bone mass
     Quality of the bone
     Diseases and medications.""",
     """Home Remedies:
     Exercises
     Vitamin D and Calcium
     Prevent falls
     Milk recipes
     """,
     ),
    ("""Peptic_Ulcer""",
     """""",
     """Common Causes:
     Bacterial infection (Helicobacter pylori)
     Non-steroidal Anti-Inflammatory Drugs like aspirin, ibuprofen (NSAIDs)
     Smoking, stress, etc., increase susceptibility
     Immune Abnormalities
     Alcoholism.""",
     """Home Remedies:
     Fenugreek leaves contain compounds that can 
     heal the ulcer. Boil 1 cup of fenugreek leaves 
     and add a pinch of salt to it. Drink this twice a day.
     Drinking raw cabbage juice is very effective for treating stomach ulcer. 
     Consume fresh cabbage juice daily before your bedtime. """,
     ),
    ("""Piles""",
     """""",
     """Common Causes:
     Low fiber diet
     Pregnancy
     Aging
     Hereditary
     Chronic constipation.""",
     """Home Remedies:
     Black Cumin Seeds Reduce Pain Associated with Piles
     Radish Juice Soothes Digestive System
     Ripe Bananas Relieve Hemorrhoid Pain
     Drink a glass of buttermilk with 1/4 tsp of carom 
     seed powder (ajwain) and a pinch of salt. Buttermilk is advised 
     as a part of the regular diet for people with piles.
     """,
     ),
    ("""Poor_Appetite""",
     """""",
     """Common Causes:
     Bacteria and viruses
     Chronic liver disease
     Depression
     Dementia
     Eating disorder
     Heart failure
     Hepatitis.""",
     """Home Remedies:
     Bitter greens such as kale, collard, endives, dandelion, arugula 
     and red or green mustard can help 
     stimulate your appetite and regulate your digestive system
     Gaining a better control over your daily routine 
     will help you get back the lost appetite.""",
     ),
    ("""Psoriasis""",
     """""",
     """Common Causes:
     The cause of psoriasis is not very well known, but 
     several risk factors increase the susceptibility of 
     the individuals to acquire psoriasis. These include 
     family history and environmental factors 
     such as smoking, stress, obesity, and alcohol consumption.""",
     """Home Remedies:
     Aloe Vera
     Apple Cider vinegar
     Capsaicin-Chili peppers are also claimed to be one of the most effective 
     and helpful herbal remedies for psoriasis.""",
     ),
    ("""Pyorrhea""",
     """""",
     """Common Causes:
     Improper brushing habits
     Poor oral hygiene
     Improper nutrition
     .""",
     """Home Remedies:
     Chewing guava leaves or unripe guava helps in curing 
     bleeding from gums and keeps the teeth healthy. It acts 
     as a teeth tonic due to the high amount of vitamin C.
     Drinking 1 cup of spinach juice mixed with 1 cup of carrot juice is another 
     effective remedy for the prevention and treatment of pyorrhea.
     """,
     ),
    ("""Quit_Smoking""",
     """""",
     """Common Causes:
     Peer pressure
     To socialize
     Association with status
     As a crutch to cope with stress or awkwardness
     Cultural reasons espoused through popular media
     .""",
     """Home Remedies:
     Black Pepper: It can actually help you overcome those 
     nicotine cravings when you’re attempting to quit smoking
     Think Positive: Your mindset has a lot to do with how successful you are in your endeavors. 
     Preparing for failure only sets you up for one. While it’s important that you don’t get disillusioned with failure, don’t try to 
     quit smoking if you don’t believe you can do it.
     """,
     ),
    ("""Gas""",
     """""",
     """Common Causes:
     Overproduction of bacteria in the stomach.
     Foods containing a lot of fiber.
     Products made with malt extracts.
     Digestive disorders such as gastroenteritis.
     Irritable bowel syndrome (IBS).""",
     """Home Remedies:
     Mix 1/2 tsp dry ginger powder with a pinch of asafoetida and a pinch of rock salt, in 1 cup of warm water. Drink.
     A drop of dill oil in a tsp of honey taken immediately after a meal will help.
     Mix 2 tsp of brandy with a cup of warm water and drink before going to bed.""",
     ),
    ("""Genital_Warts""",
     """""",
     """Common Causes:
     Skin-to-skin contact during sexual activity.
     From an infected mother to child during birth.
     Sharing of swimsuits, underwear or bath towels with the infected person.
     From hands of an infected mother to baby during activities such as diaper changing.""",
     """Home Remedies:
     mix a few drops of tea tree oil in half a bucket of water and soak in this water for about 30 minutes. This will also help to reduce the itching around warts.
     Apply a little castor oil directly on the warts and the surrounding skin before going to bed. Leave it for the night and wash in the morning. In about 2 to 3 weeks, the warts turn black and fall off.
     Onion is anti-microbial and in combination with salt, it can help in the healing of the genital warts. Soak onion (sliced sprinkled with salt) overnight, make a paste and extract the juice of this paste by passing through a sieve. Apply this juice to the genital warts everyday for about 3-4 weeks, till the warts peel off.""",
     ),
    ("""Gingivitis""",
     """""",
     """Common Causes:
     Uncontrolled diabetes greatly increases the risk.
     Hormonal changes brought on by puberty, early adulthood and pregnanc.y
     Ill-fitted dentures, braces and other oral appliances or chipped teeth, misaligned teeth and rough cavity fillings.
     Certain systemic diseases and the use of medications like phenytoin and bismuth.""",
     """Home Remedies:
     Brush your teeth.
     Floss regularly.
     Saline rinse""",
     ),
    ("""Gout""",
     """""",
     """Common Causes:
     Kidney failure.
     Hereditary factors.
     Obesity.
     Diuretics.
     High blood pressure.""",
     """Home Remedies:
     Eat 1 apple after every meal to treat gout.
     Drink a glass of lime juice in the morning,noon and night to get rid of gout.
     Drink bean juice everyday to keep gout at bay.""",
     ),
    ("""Gray_Hair""",
     """""",
     """""",
     """Home Remedies:
     Mix amla pulp with coconut oil or almond oil and massage into the scalp. This mixture will act as a colorant; and the oils will moisturize and enrich the scalp. Amla juice or amla can be cooked as a vegetable and consumed to slow or halt the growth of gray hair.
     Henna leaves or mehandi leaves is a natural auburn dye prepared from the Lawsonia inermis tree. Crushed henna leaves or powder can be made into a paste with a variety of other hair darkening substances such as lemon juice, vinegar, tea, and coffee. It is then kept overnight in an iron container, before it is applied to hair.
     Coffee can also dye your gray hair dark brown or black. Again, mix coffee decoction with henna or your hair conditioner and leave it on for a couple of hours. Repeat this once every week to get the desired color. You can also simply rinse off your hair after shampooing with cooled coffee water.""",
     ),
    ("""Hair_Loss""",
     """""",
     """Causes:
     Hairstyles: Everybody wants their hair to look good by trying different kinds of hairstyles that may look stylish, but there are some hairstyles that tend to pull the hair so tightly that they cause hair fall.
     Scalp infection: Itchy scalp may be caused due to some infections like severe dandruff and ringworm, a fungus that results in red, itchy patches on the scalp and leads to hair loss.
     Poor diet: Hair loss may also be due to poor diet that misses out on vital ingredients like proteins, iron, vitamins and minerals and other micronutrients.
     Too much stress can Trigger hair fall.""",
     """Home Remedies:
     Coconut milk: Apply coconut milk on the scalp and massage it in the hair roots. It helps in nourishing the hair and promotes hair growth.
     Henna: It is a natural hair colorant and hair conditioner. Make a mixture of henna powder, one egg and a cup of curd. Mix all these ingredients well, leave it for a night and apply the henna paste on the hair the next day. Leave it on for an hour and wash with warm water.
     Neem: Tired of your dandruff and hair fall? Try Neem, a natural antiseptic and anti-bacterial agent, which helps in treating the scalp and hair problem without any side effect. Boil 2 cups of water and add a handful of neem leaves in the boiling water. Leave till the water turns into greenish color. Use the neem water after the last rinse of your hair wash. This will keep your hair and scalp healthy.""",
     ),
    ("""Halitosis""",
     """""",
     """Causes:
     Periodontitis.
     Certain foods.
     Alcohol.
     Smoking.
      Diabetes.""",
     """Home Remedies:
     Chewing a very green Guava which is almost raw, helps.
     Chew a Green cardamom after meals for fresh breath.
     Put three whole cloves in two cups of very hot water and let it steep for 20 minutes. You can drink this clove tea or use it as a mouthwash twice a day for fresh breath.""",
     ),
    ("""Headache""",
     """""",
     """Causes:
     Several physiologic changes in the head and brain.
     Dilation and constriction of blood vessels.
     Abnormal activity of certain neurons.
     Genetic factors may be a cause for migraines.
     Smoking and alcohol may cause cluster headaches.""",
     """Home Remedies:
     Roast some caraway seeds dry. Tie in a soft handkerchief or muslin cloth and sniff to get relief from headaches.
     Add 2 teaspoons of powdered cinnamon to 1 ½ cup of milk and boil it for one or two minutes. Add a teaspoon of honey, mix and stir it thoroughly and drink it at least twice a day when suffering from a headache.
     Eating a chopped apple sprinkled with salt every morning for at least a week will help cure chronic headaches.""",
     ),
    ("""Hiccups""",
     """""",
     """Common Causes:
     Stretching of the stomach after eating or drinking.
     Sudden emotional excitement.
     Sudden change of air temperature (e.g. cool shower).
     Very hot/cold food or drink.
     Alcohol or excess smoking.""",
     """Home Remedies:
     Have a teaspoon of sugar and allow it to dissolve slowly in your mouth without chewing it. This remedy is especially for toddlers and children who are unable to follow detailed instructions on breathing pattern.
     Mix one cup of yogurt with a teaspoon of salt, stir it thoroughly until the salt dissolves completely. Have the yogurt slowly: this will help stop your hiccups.
     Peel a small piece of fresh ginger and chew on it slowly to get rid of your hiccups.""",
     ),
    ("""Hot_Flashes""",
     """""",
     """Common Causes:
     Hot flashes are caused by hormonal changes around the time of menopause. During this stage, the ovaries stop functioning. Therefore, the levels of hormones estrogen and progesterone that are normally produced by the ovaries decrease, resulting in hot flashes.""",
     """Home Remedies:
     Wear soft cotton clothes to make you feel comfortable during the attack. If the weather is cool, consider wearing a coat or a sweater, which you can remove when a hot flash begins.
     Hot flashes are usually triggered by stimuli like spicy food, coffee, alcohol etc. You may have to avoid the specific substance that triggers your hot flashes.
     Smoking can also trigger hot flashes. Therefore, avoid smoking if possible.""",
     ),
    ("""Hypothyroidism""",
     """""",
     """Common Causes:
     Hypothyroidism can be due to a number of reasons, including thyroid surgery, autoimmune disease, medications, iodine deficiency, pregnancy complications, and improper diet. Other causes can be hereditary or congenital anomaly having a dysfunctional thyroid gland at birth.
     History of hypothyroidism in the family is a more likely risk factor for developing the disease. Sometimes a tumor in the pituitary gland could stop the production of thyroid hormones. Radiation therapy may also affect thyroid gland function and cause hypothyroidism""",
     """Home Remedies:
     Include Probiotics in Diet: Probiotics are gut-friendly bacteria that help better digestion and improve metabolism. Thyroid function highly depends on how healthy is your digestive system. Improper digestion and low level of good bacteria in the stomach may reduce thyroid hormone production.
     Apple Cider Vinegar: Apple cider vinegar is good for hormone regulation and detoxification of the body. It helps lose weight, improve the metabolism of fats and carbohydrates and maintain a proper alkaline acid balance in the body. It is beneficial in controlling other chronic diseases like high cholesterol, blood pressure and diabetes.
     Exercise: Regular physical activity ensures the proper functioning of vital body organs, regulates endocrine gland functions, uplifts mood, improves metabolism, flushes body toxins and maintains a healthy weight. Few thyroid-related symptoms like fatigue, loss of appetite and osteoporosis can be combated through a regular 30-minute exercise regime.""",
     ),
    ("""Insect_Bites""",
     """Symptoms:
     Swelling.
     Localized pain.
     Redness.
     Itching.
     Rashes.""",
     """Common Causes:
     Mosquitoes.
     Fleas.
     Mites.
     Spiders.
     Bees.""",
     """Home Remedies:
     Aloe vera gel is a natural antiseptic agent that is very effective in treating insect bites. Take a fresh aloe vera leaf, simply cut it open and rub it onto the affected area to reduce the swelling, pain and itching sensation.
     Onion contains enzymes that help break down the inflammatory compounds. Cut a slice of onion and rub it over the affected part.
     Baking soda is another ingredient that is used for treating insect bites. Take a teaspoon of baking soda and add a few drops of water, mix well till it makes a paste. Apply this paste gently onto the affected area, leave for a few minutes and wash off with warm water.""",
     ),
    ("""Insomnia""",
     """""",
     """Common Causes:
     Physical - Pain, arthritis, headaches, itching, restless leg syndrome.
     Physiological - Disruptions in the sleeping environment, including light, noise, jet lag, reading heavy books etc.
     Psychological - Anxieties, depression, dementia, work related worries, relationship problems or death of closer ones.""",
     """Home Remedies:
     Eat at least 3 cups of curds daily.
     Mix 2 tsp of honey to 1 glass of warm water. Drink just before sleeping. Give half the amount to babies; it will help put them to sleep.
     Drink warm milk with honey.""",
     ),
    ("""Intestinal_Worm""",
     """Symptoms:
     Stomach pain.
     Diarrhea.
     Dysentery.
     Weight loss.
     Tiredness.""",
     """Common Causes:
     Eating contaminated food.
     Drinking contaminated water.
     Poor sanitation.
     Using human excretion as fertilizer.
     Poor personal hygiene.""",
     """Home Remedies:
     Pumpkin Seeds: Natural Remedy for Tapeworm:A mixture of ground pumpkin seeds and water can help expel tapeworms.
     Carrots are known for treating intestinal worms, as they are rich in fiber. Munch 2 carrots on an empty stomach in the morning. Doing this daily will not only help you get rid of parasites, but also prevent parasite attack in the future.
     Wormwood is a powerful herb that has been used since ancient times to treat intestinal worms. Drink a mixture of wormwood oil and olive oil to get rid of worms.""",
     ),
    ("""Itchy_Scalp""",
     """Symptoms:
     An itchy scalp is identified by an itchy sensation on the scalp, which is sometimes very severe, and is accompanied by tender, painful spots on the scalp or a burning sensation.""",
     """Common Causes:
     Fungal and/or viral infections of the scalp.
     Anxiety and stress.
     Hair lice.
     Dryness of the scalp (due to weather changes).
     Sebaceous cysts.""",
     """Home Remedies:
     Essential Oil Power- Don’t restrict the use of essential oils to just aromatherapy; a mixture of essential oils is considered a good home remedy for an itchy scalp. Choose from natural oils like lavender oil, tea tree oil, almond oil, coconut oil, avocado oil, olive oil and peppermint oil.
     Lemon Goodness- Yet another powerful home remedy for treating an itchy scalp is the lemon. Simply squeeze a lemon, and apply its juice directly to your scalp before shampooing. This home remedy is effective in treating dandruff too!
     Apple Cider to the Rescue- You may find apple cider vinegar cropping up in the home remedies section of almost every condition; and why not? With its powerful anti-inflammatory properties and its natural goodness, apple cider is truly a star!""",
     ),
    ("""Itchy_Skin""",
     """""",
     """Common Causes:
     Skin lesions.
     Dry skin.
     Internal illnesses.
     Pregnancy.
     Menopause.""",
     """Home Remedies:
     Apple cider vinegar (ACV) is an effective antiseptic agent that helps relieve dry and itchy skin. Dab a cotton ball on the vinegar and apply on the itchy area, this will help the itching go away.
     Aloe vera works wonders to treat itchy skin. Just slice a piece of aloe vera and rub the gel on the affected skin. This helps to relieve the irritation and swelling of the skin.
     Basil leaves contain a substance called eugenol, which is a very effective topical anesthetic. Boil some basil leaves into a tea, allowing it to cool, then use a cotton ball and apply on the itching part.""",
     ),
    ("""Jaundice""",
     """""",
     """Common Causes:
     The red blood cells after a period of 4 months' time becomes fragile and become a yellow-colored chemical called Bilirubin. The body usually removes bilirubin from the bloodstream by passing it through the liver and to the kidneys for disposal. The liver, which plays a vital role in removing the bilirubin from the body, may not be able to do so for some reasons, where the bilirubin gets accumulated and causes jaundice.""",
     """Home Remedies:
     1/4 tsp of turmeric powder mixed in a glass of hot water taken 2-3 times a day.
     Make a paste of tender papaya leaves. Take 1/2 tsp of this paste with 1 tsp honey.
     Boil 1 cup of water, when it boils add 8-10 lemon leaves. Cover and leave for 4-5 minutes. Drink the decoction for 4-5 days.""",
     ),
    ("""Kidney_Stones""",
     """""",
     """Common Causes:
     Urinary tract infection (UTI).
     Overdoses of vitamin D.
     Mineral imbalance.
     Kidney disease.
     Dehydration.""",
     """Home Remedies:
     Basil Leaves Good for Kidney Health:Basil leaves (Tulsi) are good for the overall health of kidneys. Mix 1 teaspoon of juice from basil leaves with 1 teaspoon of honey and have it daily in the morning. You can also chew two to three basil leaves in order to remove the stones from the urinary tract.
     Watermelon Juice Helps Flush Out Kidney Stones:The water and potassium content present in watermelon are essential nutrients for a healthy kidney. It helps in regulating and maintaining the level of acid present in the urine. Eating watermelon or drinking its juice every day will help in flushing out stones from the kidney.
     Figs for Dissolving Kidney Stones:Boil two figs in a cup of water and drink it on an empty stomach early in the morning.""",
     ),
    ("""Vertigo""",
     """""",
     """"Common Causes:
     An infection in ear for example syphilis.
     Due to the free-floating calcium carbonate crystals in the posterior semicircular canals of the inner ear.
     Brain Tumors, Acute head injury, Thyroid, Anemia.""",
     """Home Remedies:
     Soak 1 tsp of amla (gooseberry) powder in water along with 1 tsp coriander seeds. Leave overnight. Strain and add 1/2 tsp sugar and drink.
     Try to relax your body and make sure you have enough sleep because lack of sleep can aggravate vertigo and cause sudden dizziness and nausea.
     High intake of liquids such as juice and water prevents dizziness.""",
     ),
    ("""Vomiting""",
     """""",
     """Common Causes:
     Food Poisoning.
     Pregnancy
     Disgusting sights and smells
     Certain drugs""",
     """Home Remedies:
     Heat 2 cardamoms on a dry saucepan. Powder them and add a tablespoon of honey and take frequently.
     Try mint tea to get relief from vomiting. Add mint leaves in boiling water. Strain the leaves and serve your tea.
     Ginger is another ingredient to cure the problem of vomiting. Ginger is good for your digestive system and helps to block unnecessary secretion inside the stomach that can cause vomiting.""",
     ),
    ("""Whiteheads""",
     """""",
     """Common Causes:
     Hormonal Changes
     Medications
     Excessive use of cosmetics
     Poor Hygiene""",
     """Home Remedies:
     Baking Soda exfoliates your skin and helps get rid of dead skin cells. It also maintains the pH balance of your skin.
     Oatmeal opens your pores and prevents it from clogging. It also absorbs excess oil secretion and serves as an excellent scrub.
     Rich in ascorbic acid, lemon juice can help reduce whiteheads. Extract the juice of a lemon into a small bowl and apply it on the affected areas of your skin using a piece of clean cotton.""",
     ),
    ("""Yeast_Infection""",
     """Symptoms:
     Oral candida infections are usually characterized by development of cracks at the corners of the mouth, white spots inside the mouth and tongue, soreness of the throat accompanied by difficulty in swallowing and redness and discomfort in the mouth.
     """,
     """Common Causes:
     antibiotics are believed to be the major culprits in causing a yeast infection. They do this by disturbing the normal healthy microorganisms and making conditions favorable for the growth of candida.
     Many other factors such as lack of sleep, stress, overconsumption of alcohol, refined sugar etc, too, may lead to development of yeast infections.""",
     """Home Remedies:
     Use warm water and soap to clean the affected parts thoroughly, and wear clean, dry underwear made of breathable fabrics. You may also try boric acid as a remedy to curb recurrent yeast infections.
     Wipe your sweat often and avoid staying too long in wet clothes. Use antifungal powders and creams on areas that are moist and more prone to yeast infections. Avoid wearing tight clothing-choose light, loose, soft fabrics that are clean.
     """,
     ),
    ("""Rheumatism""",
     """""",
     """""",
     """Home remedies:
     Eat a healthy diet that contains vitamins and minerals like whole grain, fruits and veggies, olive oil, beans, herbs and spices to support your body's healing efforts.
     Exercising will keep your body flexible and energetic and help maintain good movement that can reduce the pain and risk of joint injury.
     A warm bath or shower can provide relief from joint pain.
     Add 2 teaspoons of apple cider vinegar and honey in a glass of warm water. Have this mixture once or twice a day.""",
     ),
    ("""Ringworm""",
     """""",
     """Common Causes:
     Through scratches or cuts in the skin.
     Affects damp areas where sweating is common.
     Using unwashed clothes or sharing combs of infected people.
     Swimming pool.""",
     """Home Remedies:
     Rub a slice of freshly cut raw papaya on the patch.
     Make a powder with mustard seeds. Add some water to the powder and make a paste. Apply on the patch till it disappears.
     The juice of basil leaves (tulsi) to be applied on the patch 2-3 times a day.
     Turmeric has great natural antibiotic qualities. Extract the juice from fresh turmeric and apply to the areas that are affected until you see the problem go away.""",
     ),
    ("""Rosacea""",
     """""",
     """Common causes:
     Alcohol consumption.
     Eating spicy foods.
     
     Hot baths.
     Extreme temperatures.
     Intense workout routines.
     Drinking hot beverages.""",
     """Home Remedies:
     The anti-inflammatory properties present in chamomile helps reduce redness caused by rosacea.
     Green tea with its antioxidant, anti-carcinogenic and anti-inflammatory properties is helpful in many skin conditions including rosacea.
     Boil some green tea leaves, cool the solution and refrigerate. Use it as cold compress for relief from rosacea.
     Cucumber, with its cooling properties gives relief from discomfort caused by rosacea symptoms.""",
     ),
    ("""Skin_pigmentation""",
     """""",
     """Common causes:
     The melanin production goes awry; either too little or too much melanin is produced, causing skin pigmentation disorders.
     The precursors of many disorders, are also known to cause skin pigmentation disorders.
     Skin pigmentation disorders is accompanied by several itching.""",
     """Home remedies:
     Grate the skin of an orange and make a paste/gel with few teaspoons of milk. Leave it on for half an hour and then massage gently and wash it off with warm water. Exfoliate your face at least 3 to 4 times a week with this paste. Exfoliation encourages cell renewal and removes the dark blotches.
     Make a face pack with almond and honey. Apply and wash it off after 15 minutes
     Sunlight worsens the condition, so use sunscreen at all times.""",
     ),
    ("""Snoring""",
     """""",
     """Common causes:
     Pregnancy.
     Stress.
     Distribution of fat in the body.
     Low levels of estrogen/progesterone.
     Menopause.
     Age.""",
     """Home remedies:
     Snoring may be reduced with homeopathic medications with an efficacy rate of 80%.
     Snoring is reduced with oropharyngeal sprays. These sprays have an efficacy rate of 30%.
     Avoid alcohol.""",
     ),
    ("""Sore_Throat""",
     """""",
     """Common causes:
     Viral infection.
     Bacterial infection.
     Fungal infection.
     Smoking.""",
     """Home Remedies:
     Drink ginger tea.
     Inhaling fragrances of essential oils can treat your sore throat.
     Add honey and lemon juice to 1 cup of warm water, as it works best for sore throat."""
     ),
    ("""Sprains""",
     """""",
     """Common causes:
     Running or walking on uneven ground.
     Wearing high-heeled shoes.
     Overstretching of a ligament.
     During a fall.
     Lifting heavy weight.""",
     """Home remedies:
     Chop onions, wrap them in a muslin cloth and place on the sprained area.
     Make a paste of ground lemon leaves and butter. Apply on the affected area.
     Mix 1 teaspoon of almond oil with 1 teaspoon of garlic oil and apply on the injured area.""",
     ),
    ("""Staph_infection""",
     """""",
     """Common causes:
     Using infected objects, towels, clothes, utensils, etc.
     Drug abuse - injecting infected needles.
     Low immunity due to any medical condition.
     Using an internal medical device such as catheter, feeding tube or fitted artificial joint.
     Sharing gym and sports equipment.""",
     """Home remedies:
     Cotton soaked in apple cider vinegar applied over an infected region or mix with baking soda and apply it as a paste to rapidly reduce pain and discomfort.
     Another bactericidal herb is tea tree. Its oil decreases the growth of bacteria reducing the effects of staph infection.""",
     ),
    ("""Stretch_marks""",
     """""",
     """common causes:
     Pregnancy and stretch marks go together. The rapid weight gain coupled with many hormonal changes during pregnancy cause stretch marks.
     Weight gain during puberty is caused by hormonal changes and this often results in stretch marks in both girls and boys.
     Intake of oral or systemic steroids and use of medications such as Corticosteroid pills, creams and lotions can cause stretch marks.""",
     """home remedies:
     The benefits of aloe vera for health and beauty are now well known. The gel from aloe plant can also help lighten stretch marks if used on a regular basis on the affected areas.
     The acidity in lemon juice helps lighten scars and marks and this can help reduce the appearance of stretch marks as well.
     Massage affected areas with castor oil and keep it overnight. For more effective results apply some heat over it using a hot water bottle.
     Full of Vitamin A and protein, egg whites can help reduce the appearance of stretch marks.""",
     ),
    ("""Stuffy_Nose""",
     """""",
     """Common causes:
     Flu.
     Common cold.
     Sinusitis-Acute and chronic.""",
     """Home remedies:
     In the case of children, the pillow should be raised to elevate the childss head and ease the discomfort of the congestion in the nose.
     In Dry climates, a humidifier is recommended to moisten the nasal passages and avoid the congestion of the nose.
     Mucus should be removed at regular intervals. Older children may be asked to blow their noses. However, an aspirator should be used for infants.""",
     ),
    ("""Sun_burns""",
     """""",
     """Common causes:
     Ultra violet rays of the sun.
     direct sunlight.""",
     """home remedies:
     A dampened towel with cool water or cotton pads soaked in cool but not chilled water should be applied as soon as possible to the affected area. Repeat for few minutes and apply several times in day.
     Fat free milk mixed with cold water can also be applied to affected area. This must be applied 2-4 times in a day to reduce the burning sensation and inflammation.
     Drinking plenty of fluids will help in easing out the effects of sun exposure and keep the skin hydrated.""",
     ),
    ("""Toothache""",
     """""",
     """Common causes:
     Dental decay.
     Dental cavities.
     Swelling of the pulp.
     Tooth infection.
     Broken tooth.""",
     """Home remedies:
     Garlic has antibiotics and other medicinal properties that can be very effective for treating toothache. Crush a clove of garlic with rock salt and apply on the affected tooth.
     Place a piece of raw onion on the tooth. This will help in killing the germs in the affected tooth and offer relief from pain.
     Mix equal amounts of pepper, salt and few drops of water to form a paste. Apply this paste on the affected area. This will help relieve the toothache.""",
     ),
    ("""Upset_stomach""",
     """""",
     """Common causes:
     Alcohol excess.
     Barbiturate abuse.
     Food poisoning.
     Gastritis.
     Pregnancy.
     Stress.""",
     """Home remedies:
     Baking soda is a common home remedy for treating upset stomach.
     Papaya fruit contains papain, an enzyme that helps break down protein and soothe the stomach. It aid in digestion, eases indigestion and also helps with constipation.
     Herbal teas such as ginger, sage, chamomile, peppermint and so on work wonder to ease down abdominal problems. They also relieve cramping stomach and intestinal muscles. Make some herbal tea and have it daily.""",
     ),
    ("""Urinary_tract_infection""",
     """""",
     """Common causes:
     Dieabetes.
     pregnancy.
     Most commonly, it occurs as a result of bacterial invasion into the urinary tract, which is common during sexual activity with an infected person.""",
     """Home remedies:
     People suffering from frequent, recurring UTI can benefit a lot by using yogurt as a home remedy.
     The lactobacilli-bacteria present in the yogurt, are thought to reduce the occurrence of urinary tract infection.""",
     )
]

add_many(stuff)
