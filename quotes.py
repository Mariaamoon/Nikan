"""
Quote dataset — each quote has:
  - text:   the quote itself
  - author: who said it
  - topics: list of topic tags
  - mood:   emotional tone
  - length: 'short' | 'medium' | 'long'
"""

QUOTES =[
      {
        "text": 'Awake! for Morning in the Bowl of Night has flung the Stone that puts the Stars to Flight.',
        "author": 'Omar Khayyam',
        "mood": 'awakening',
    },
    {
        "text": 'A Book of Verses underneath the Bough, a Jug of Wine, a Loaf of Bread—and Thou beside me singing in the Wilderness.',
        "author": 'Omar Khayyam',
        "mood": 'love',
    },
    {
        "text": 'The Moving Finger writes; and, having writ, moves on: nor all thy Piety nor Wit shall lure it back to cancel half a Line.',
        "author": 'Omar Khayyam',
        "mood": 'fate',
    },
    {
        "text": 'Ah, fill the Cup:—what boots it to repeat how Time is slipping underneath our Feet.',
        "author": 'Omar Khayyam',
        "mood": 'time',
    },
    {
        "text": "One Moment in Annihilation's Waste, One Moment, of the Well of Life to taste.",
        "author": 'Omar Khayyam',
        "mood": 'mortality',
    },
    {
        "text": "Ah, Love! could thou and I with Fate conspire to grasp this sorry Scheme of Things entire, would not we shatter it to bits—and then re-mould it nearer to the Heart's Desire!",
        "author": 'Omar Khayyam',
        "mood": 'love',
    },
    {
        "text": "The Worldly Hope men set their Hearts upon turns Ashes—or it prospers; and anon, like Snow upon the Desert's dusty Face, lighting a little Hour or two—is gone.",
        "author": 'Omar Khayyam',
        "mood": 'impermanence',
    },
    {
        "text": 'Myself when young did eagerly frequent Doctor and Saint, and heard great Argument about it and about: but evermore came out by the same Door as in I went.',
        "author": 'Omar Khayyam',
        "mood": 'wisdom',
    },
    {
        "text": 'I came like Water, and like Wind I go.',
        "author": 'Omar Khayyam',
        "mood": 'impermanence',
    },
    {
        "text": 'Into this Universe, and why not knowing, nor whence, like Water willy-nilly flowing.',
        "author": 'Omar Khayyam',
        "mood": 'wonder',
    },
    {
        "text": 'There was a Door to which I found no Key: there was a Veil past which I could not see.',
        "author": 'Omar Khayyam',
        "mood": 'longing',
    },
    {
        "text": 'Drink! for you know not whence you came, nor why: Drink! for you know not why you go, nor where.',
        "author": 'Omar Khayyam',
        "mood": 'mystery',
    },
    {
        "text": 'We are no other than a moving row of visionary Shapes that come and go round with this Sun-illumined Lantern held in Midnight by the Master of the Show.',
        "author": 'Omar Khayyam',
        "mood": 'wonder',
    },
    {
        "text": "Yesterday This Day's Madness did prepare; To-morrow's Silence, Triumph, or Despair.",
        "author": 'Omar Khayyam',
        "mood": 'time',
    },
    {
        "text": 'And if the Wine you drink, the Lip you press, end in the Nothing all Things end in—Yes.',
        "author": 'Omar Khayyam',
        "mood": 'mortality',
    },
    {
        "text": 'I sometimes think that never blows so red the Rose as where some buried Caesar bled.',
        "author": 'Omar Khayyam',
        "mood": 'mortality',
    },
    {
        "text": "Think, in this batter'd Caravanserai whose Doorways are alternate Night and Day, how Sultan after Sultan with his Pomp abode his Hour or two, and went his way.",
        "author": 'Omar Khayyam',
        "mood": 'impermanence',
    },
    {
        "text": 'The Bird of Time has but a little way to fly—and Lo! the Bird is on the Wing.',
        "author": 'Omar Khayyam',
        "mood": 'time',
    },
    {
        "text": 'Lo! some we loved, the loveliest and the best that Time and Fate of all their Vintage prest, have drunk their Cup a Round or two before, and one by one crept silently to Rest.',
        "author": 'Omar Khayyam',
        "mood": 'loss',
    },
    {
        "text": 'Ah, make the most of what we yet may spend, before we too into the Dust descend.',
        "author": 'Omar Khayyam',
        "mood": 'joy',
    },
    {
        "text": 'Look to the Rose that blows about us—Lo, Laughing, she says, into the World I blow.',
        "author": 'Omar Khayyam',
        "mood": 'joy',
    },
    {
        "text": 'How sweet is mortal Sovranty!—think some: Others—How blest the Paradise to come!',
        "author": 'Omar Khayyam',
        "mood": 'wisdom',
    },
    {
        "text": 'Better, oh, better, cancel from the Scroll of Universe one luckless Human Soul, than drop by drop enlarge the Flood that rolls hoarser with Anguish as the Ages Roll.',
        "author": 'Omar Khayyam',
        "mood": 'compassion',
    },
    {
        "text": "'Tis all a Chequer-board of Nights and Days where Destiny with Men for Pieces plays.",
        "author": 'Omar Khayyam',
        "mood": 'fate',
    },
    {
        "text": 'And the first Morning of Creation wrote what the Last Dawn of Reckoning shall read.',
        "author": 'Omar Khayyam',
        "mood": 'fate',
    },
    {
        "text": 'When You and I behind the Veil are past, oh, but the long long while the World shall last.',
        "author": 'Omar Khayyam',
        "mood": 'mortality',
    },
    {
        "text": "I think the Vessel, that with fugitive Articulation answer'd, once did live, and merry-make.",
        "author": 'Omar Khayyam',
        "mood": 'wonder',
    },
    {
        "text": "Indeed the Idols I have loved so long have done my Credit in Men's Eye much wrong.",
        "author": 'Omar Khayyam',
        "mood": 'regret',
    },
    {
        "text": "Alas, that Spring should vanish with the Rose! That Youth's sweet-scented Manuscript should close!",
        "author": 'Omar Khayyam',
        "mood": 'loss',
    },
    {
        "text": "Strange, is it not? that of the myriads who before us pass'd the door of Darkness through, not one returns to tell us of the Road.",
        "author": 'Omar Khayyam',
        "mood": 'mystery',
    },
    {
        "text": 'I sent my Soul through the Invisible, some letter of that After-life to spell.',
        "author": 'Omar Khayyam',
        "mood": 'wonder',
    },
    {
        "text": "Heav'n but the Vision of fulfill'd Desire, and Hell the Shadow of a Soul on fire.",
        "author": 'Omar Khayyam',
        "mood": 'wisdom',
    },
    {
        "text": 'A Hair perhaps divides the False and True; and upon what, prithee, may life depend?',
        "author": 'Omar Khayyam',
        "mood": 'wisdom',
    },
    {
        "text": 'Waste not your Hour, nor in the vain pursuit of This and That endeavour and dispute; better be jocund with the fruitful Grape than sadden after none, or bitter, Fruit.',
        "author": 'Omar Khayyam',
        "mood": 'joy',
    },
    {
        "text": 'And not a drop that from our Cups we throw on the parcht herbage but may steal below to quench the fire of Anguish in some Eye there hidden—far beneath, and long ago.',
        "author": 'Omar Khayyam',
        "mood": 'compassion',
    },
    {
        "text": "Ah, Moon of my Delight, who know'st no wane, the Moon of Heav'n is rising once again.",
        "author": 'Omar Khayyam',
        "mood": 'love',
    },
    {
        "text": 'With me along some Strip of Herbage strown that just divides the desert from the sown, where name of Slave and Sultan scarce is known.',
        "author": 'Omar Khayyam',
        "mood": 'peace',
    },
    {
        "text": "And David's Lips are lock't; but in divine High piping Pehlevi, with Wine! Wine! Wine! Red Wine!—the Nightingale cries to the Rose.",
        "author": 'Omar Khayyam',
        "mood": 'joy',
    },
    {
        "text": 'A true lover is proved such by his pain of heart; no sickness is there like sickness of heart.',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'However much we describe and explain love, when we fall in love we are ashamed of our words.',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'None but the sun can display the sun. If you would see it displayed, turn not away from it.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'Love exalts our earthly bodies to heaven, and makes the very hills to dance with joy!',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'Hail to thee, then, O LOVE, sweet madness! Thou who healest all our infirmities!',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'Body is not veiled from soul, neither soul from body, yet no man hath ever seen a soul.',
        "author": 'Rumi',
        "mood": 'wonder',
    },
    {
        "text": 'Arise, O son! burst thy bonds and be free! How long wilt thou be captive to silver and gold?',
        "author": 'Rumi',
        "mood": 'freedom',
    },
    {
        "text": 'Knowest thou why thy mirror reflects not? Because the rust has not been scoured from its face.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'The flute is the confidant of all unhappy lovers; yea, its strains lay bare my inmost secrets.',
        "author": 'Rumi',
        "mood": 'longing',
    },
    {
        "text": 'Through grief my days are as labor and sorrow, my days move on, hand in hand with anguish.',
        "author": 'Rumi',
        "mood": 'grief',
    },
    {
        "text": 'Happy the soul who for love of God has lavished family, wealth, and goods!',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": "Watch the face of each one, regard it well, it may be by serving thou wilt recognize Truth's face.",
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'My heart says, He has injured me, but I laugh at these pretended injuries.',
        "author": 'Rumi',
        "mood": 'acceptance',
    },
    {
        "text": 'I am enamoured of my own grief and pain, for it makes me well-pleasing to my peerless King.',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'The tears which are shed because of His chastening are very pearls, though men deem them mere tears.',
        "author": 'Rumi',
        "mood": 'grief',
    },
    {
        "text": 'Every night Thou freest our spirits from the body and its snare, making them pure as rased tablets.',
        "author": 'Rumi',
        "mood": 'peace',
    },
    {
        "text": "If thou hadst Majnun's eyes, the two worlds would be within thy view.",
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'In love to be wide awake is treason. The more a man is awake, the more he sleeps to love.',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'Love and tenderness are qualities of humanity, passion and lust are qualities of animality.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": "Woman is a ray of God, not a mere mistress, the Creator's self, as it were, not a mere creature!",
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'Nothing is bitterer than severance from Thee, without Thy shelter there is naught but perplexity.',
        "author": 'Rumi',
        "mood": 'longing',
    },
    {
        "text": 'A life living without Thee esteem as dead!',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'If Thou findest fault with Thy slaves, verily it is right in Thee, O Blessed One!',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'When the rose has faded and the garden is withered, the song of the nightingale is no longer to be heard.',
        "author": 'Rumi',
        "mood": 'loss',
    },
    {
        "text": 'LOVE desires that this secret should be revealed, for if a mirror reflects not, of what use is it?',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'The kingly soul lays waste the body, and after its destruction he builds it anew.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'Who can describe the unique work of Grace? I have been forced to illustrate it by these similes.',
        "author": 'Rumi',
        "mood": 'wonder',
    },
    {
        "text": 'When love of God kindles a flame in the inward man, he burns, and is freed from effects.',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'He has no need of signs to assure him of love, for love casts its own light up to heaven.',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'Reason has no care for these matters, in its mind is naught but regard to Allah.',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'Such is the power of the soul, O man of right views! Then what is the power of the Soul of souls?',
        "author": 'Rumi',
        "mood": 'wonder',
    },
    {
        "text": "If the heart opens the mouth of mystery's store, the soul springs up swiftly to highest heaven.",
        "author": 'Rumi',
        "mood": 'wonder',
    },
    {
        "text": 'Whoso recognizes and confesses his own defects is hastening in the way that leads to perfection!',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'No sickness worse than fancying thyself perfect can infect thy soul, O arrogant misguided one!',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'Make yourself pure from all attributes of self, that you may see your own pure bright essence!',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'The knowledge of men of heart bears them up, the knowledge of men of the body weighs them down.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'If you want an instance of this secret knowledge, hear the story of the Greeks and the Chinese.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'There is no anger in my soul against thee, because I attribute not this deed to thee.',
        "author": 'Rumi',
        "mood": 'forgiveness',
    },
    {
        "text": 'Out of darkness was created light.',
        "author": 'Rumi',
        "mood": 'hope',
    },
    {
        "text": 'If He crushes His own instruments, He makes those crushed ones fair in His sight.',
        "author": 'Rumi',
        "mood": 'acceptance',
    },
    {
        "text": 'O Aider of aid-seekers, guide us, for there is no security in knowledge or wealth.',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'When the heart is garnished and swept clear of lust, therein the God of Mercy sitteth on His throne.',
        "author": 'Rumi',
        "mood": 'peace',
    },
    {
        "text": 'Our senses and our endless discourses are annihilated in the light of the knowledge of our King.',
        "author": 'Rumi',
        "mood": 'wonder',
    },
    {
        "text": 'All pressing on from Not-being to Being, on the last day, as well the thankful as the unthankful.',
        "author": 'Rumi',
        "mood": 'hope',
    },
    {
        "text": "Fear then, and revile not the wicked, for the wicked are impotent under God's commands.",
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'Scoff not nor chide even them that go astray!',
        "author": 'Rumi',
        "mood": 'compassion',
    },
    {
        "text": 'There is no security in knowledge or wealth; lead not our hearts astray after Thou hast guided us.',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'Our worldly goods rob us of our heavenly goods, our body rends the garment of our soul.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'Without reliance on Thee how can we live?',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'If Thou showest not the way, our life is lost.',
        "author": 'Rumi',
        "mood": 'longing',
    },
    {
        "text": "Since thy 'self' has not yet left thee, thou must be burned in fiery flames.",
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": "There is not room for two I's in one house.",
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'Defects are the mirrors of the attributes of Beauty, the base is the mirror of the High and Glorious One.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'Shed many tears of blood from eyes and heart, that this self-satisfaction may be driven out.',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'If you drink not His cup, how will you escape lusts?',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'Look for the moon in heaven, not in the water!',
        "author": 'Rumi',
        "mood": 'wisdom',
    },
    {
        "text": 'If you desire to rise above mere names and letters, make yourself free from self at one stroke!',
        "author": 'Rumi',
        "mood": 'freedom',
    },
    {
        "text": 'Love signifies the strong attraction that draws all creatures back to reunion with their Creator.',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": 'The BELOVED is all in all, the lover only veils Him; the BELOVED is all that lives, the lover a dead thing.',
        "author": 'Rumi',
        "mood": 'devotion',
    },
    {
        "text": 'Did my Beloved only touch me with his lips, I too, like the flute, would burst out in melody.',
        "author": 'Rumi',
        "mood": 'love',
    },
    {
        "text": "When the lover feels no longer LOVE's quickening, he becomes like a bird who has lost its wings.",
        "author": 'Rumi',
        "mood": 'longing',
    },
    {
        "text": 'How can I retain my senses about me, when the BELOVED shows not the light of His countenance?',
        "author": 'Rumi',
        "mood": 'longing',
    },
    {
        "text": 'I depart as air, I shake my white locks at the runaway sun, I effuse my flesh in eddies, and drift it in lacy jags.',
        "author": 'Walt Whitman',
        "mood": 'awakening',
    },
    {
        "text": 'Long have you timidly waded holding a plank by the shore, now I will you to be a bold swimmer.',
        "author": 'Walt Whitman',
        "mood": 'awakening',
    },
    {
        "text": 'I am he that walks with the tender and growing night, I call to the earth and sea half-held by the night.',
        "author": 'Walt Whitman',
        "mood": 'awakening',
    },
    {
        "text": 'Let nothing be done rashly, and at random, but all things according to the most exact and perfect rules of art.',
        "author": 'Marcus Aurelius',
        "mood": 'awakening',
    },
    {
        "text": 'Whatsoever doth happen in the world, doth happen justly.',
        "author": 'Marcus Aurelius',
        "mood": 'fate',
    },
    {
        "text": 'Such and such things, from such and such causes, must of necessity proceed.',
        "author": 'Marcus Aurelius',
        "mood": 'fate',
    },
    {
        "text": 'That lot and portion which is assigned to every one, as it is unavoidable and necessary, so is it always profitable.',
        "author": 'Marcus Aurelius',
        "mood": 'fate',
    },
    {
        "text": 'Willingly therefore, and wholly surrender up thyself unto that fatal concatenation, yielding up thyself unto the fates, to be disposed of at their pleasure.',
        "author": 'Marcus Aurelius',
        "mood": 'fate',
    },
    {
        "text": 'There was never any more inception than there is now, nor any more youth or age than there is now.',
        "author": 'Walt Whitman',
        "mood": 'time',
    },
    {
        "text": "The time of a man's life is as a point; the substance of it ever flowing, the sense obscure.",
        "author": 'Marcus Aurelius',
        "mood": 'time',
    },
    {
        "text": 'No man properly can be said to live more than that which is now present, which is but a moment of time.',
        "author": 'Marcus Aurelius',
        "mood": 'time',
    },
    {
        "text": 'The age and time of the world is as it were a flood and swift current, consisting of the things that are brought to pass in the world.',
        "author": 'Marcus Aurelius',
        "mood": 'time',
    },
    {
        "text": 'Sunset and evening star, and one clear call for me! And may there be no moaning of the bar, when I put out to sea.',
        "author": 'Alfred, Lord Tennyson',
        "mood": 'mortality',
    },
    {
        "text": 'I hope to see my Pilot face to face when I have crost the bar.',
        "author": 'Alfred, Lord Tennyson',
        "mood": 'mortality',
    },
    {
        "text": 'Twilight and evening bell, and after that the dark! And may there be no sadness of farewell, when I embark.',
        "author": 'Alfred, Lord Tennyson',
        "mood": 'mortality',
    },
    {
        "text": 'Because I could not stop for Death, He kindly stopped for me; the Carriage held but just Ourselves and Immortality.',
        "author": 'Emily Dickinson',
        "mood": 'mortality',
    },
    {
        "text": 'Consider how quickly all things are dissolved and resolved: the bodies and substances themselves, into the matter and substance of the world.',
        "author": 'Marcus Aurelius',
        "mood": 'impermanence',
    },
    {
        "text": 'This world is mere change, and this life, opinion.',
        "author": 'Marcus Aurelius',
        "mood": 'impermanence',
    },
    {
        "text": 'As soon as anything hath appeared, and is passed away, another succeeds, and that also will presently out of sight.',
        "author": 'Marcus Aurelius',
        "mood": 'impermanence',
    },
    {
        "text": 'Within a very little while, both thou and he shall both be dead, and after a little while more, not so much as your names and memories shall be remaining.',
        "author": 'Marcus Aurelius',
        "mood": 'impermanence',
    },
    {
        "text": 'To see a World in a Grain of Sand and a Heaven in a Wild Flower, hold Infinity in the palm of your hand and Eternity in an hour.',
        "author": 'William Blake',
        "mood": 'wonder',
    },
    {
        "text": 'I believe a leaf of grass is no less than the journey-work of the stars.',
        "author": 'Walt Whitman',
        "mood": 'wonder',
    },
    {
        "text": 'A mouse is miracle enough to stagger sextillions of infidels.',
        "author": 'Walt Whitman',
        "mood": 'wonder',
    },
    {
        "text": 'I hear and behold God in every object, yet understand God not in the least.',
        "author": 'Walt Whitman',
        "mood": 'wonder',
    },
    {
        "text": "I am enamour'd of growing out-doors, of men that live among cattle or taste of the ocean or woods.",
        "author": 'Walt Whitman',
        "mood": 'longing',
    },
    {
        "text": 'Remember me when I am gone away, gone far away into the silent land.',
        "author": 'Christina Rossetti',
        "mood": 'longing',
    },
    {
        "text": 'Remember me when no more day by day you tell me of our future that you planned.',
        "author": 'Christina Rossetti',
        "mood": 'longing',
    },
    {
        "text": "I am he attesting sympathy, extoller of amies and those that sleep in each others' arms.",
        "author": 'Walt Whitman',
        "mood": 'longing',
    },
    {
        "text": 'There is, who without so much as a coat; and there is, who without so much as a book, doth put philosophy in practice.',
        "author": 'Marcus Aurelius',
        "mood": 'mystery',
    },
    {
        "text": 'If the souls remain after death, how is the air from all eternity able to contain them?',
        "author": 'Marcus Aurelius',
        "mood": 'mystery',
    },
    {
        "text": 'What is it then that shall always be remembered? all is vanity.',
        "author": 'Marcus Aurelius',
        "mood": 'mystery',
    },
    {
        "text": 'It is for my mouth forever, I am in love with it, I will go to the bank by the wood and become undisguised and naked.',
        "author": 'Walt Whitman',
        "mood": 'mystery',
    },
    {
        "text": 'Yet if you should forget me for a while and afterwards remember, do not grieve.',
        "author": 'Christina Rossetti',
        "mood": 'loss',
    },
    {
        "text": 'Better by far you should forget and smile than that you should remember and be sad.',
        "author": 'Christina Rossetti',
        "mood": 'loss',
    },
    {
        "text": 'For some we loved, the loveliest and the best that from his Vintage rolling Time hath prest, have drunk their Cup a Round or two before, and one by one crept silently to rest.',
        "author": 'Omar Khayyam',
        "mood": 'loss',
    },
    {
        "text": 'It will be late to counsel then or pray.',
        "author": 'Christina Rossetti',
        "mood": 'loss',
    },
    {
        "text": 'I celebrate myself, and sing myself, and what I assume you shall assume, for every atom belonging to me as good belongs to you.',
        "author": 'Walt Whitman',
        "mood": 'joy',
    },
    {
        "text": 'I loafe and invite my soul, I lean and loafe at my ease observing a spear of summer grass.',
        "author": 'Walt Whitman',
        "mood": 'joy',
    },
    {
        "text": 'I am satisfied, I see, dance, laugh, sing.',
        "author": 'Walt Whitman',
        "mood": 'joy',
    },
    {
        "text": 'I dote on myself, there is that lot of me and all so luscious, each moment and whatever happens thrills me with joy.',
        "author": 'Walt Whitman',
        "mood": 'joy',
    },
    {
        "text": 'He it was also that did put me in the first conceit and desire of an equal commonwealth, administered by justice and equality.',
        "author": 'Marcus Aurelius',
        "mood": 'compassion',
    },
    {
        "text": 'Whatsoever proceeds from men, as they are our kinsmen, should by us be entertained, with love, always.',
        "author": 'Marcus Aurelius',
        "mood": 'compassion',
    },
    {
        "text": 'It is part of justice to bear with them, and that it is against their wills that they offend.',
        "author": 'Marcus Aurelius',
        "mood": 'compassion',
    },
    {
        "text": 'The kept-woman, sponger, thief, are hereby invited. There shall be no difference between them and the rest.',
        "author": 'Walt Whitman',
        "mood": 'compassion',
    },
    {
        "text": 'Backward I see in my own days where I sweated through fog with linguists and contenders, I have no mockings or arguments, I witness and wait.',
        "author": 'Walt Whitman',
        "mood": 'regret',
    },
    {
        "text": 'Having fallen into some fits of love, I was soon cured.',
        "author": 'Marcus Aurelius',
        "mood": 'regret',
    },
    {
        "text": 'Having been often displeased, I never did anything for which afterwards I had occasion to repent.',
        "author": 'Marcus Aurelius',
        "mood": 'regret',
    },
    {
        "text": 'Spend not the remnant of thy days in thoughts and fancies concerning other men.',
        "author": 'Marcus Aurelius',
        "mood": 'regret',
    },
    {
        "text": 'But such a tide as moving seems asleep, too full for sound and foam, when that which drew from out the boundless deep turns again home.',
        "author": 'Alfred, Lord Tennyson',
        "mood": 'peace',
    },
    {
        "text": 'A man cannot any whither retire better than to his own soul.',
        "author": 'Marcus Aurelius',
        "mood": 'peace',
    },
    {
        "text": 'By tranquillity I understand a decent orderly disposition and carriage, free from all confusion and tumultuousness.',
        "author": 'Marcus Aurelius',
        "mood": 'peace',
    },
    {
        "text": 'At what time soever thou wilt, it is in thy power to retire into thyself, and to be at rest, and free from all businesses.',
        "author": 'Marcus Aurelius',
        "mood": 'peace',
    },
    {
        "text": 'From Apollonius, true liberty, and unvariable steadfastness, and not to regard anything at all, though never so little, but right and reason.',
        "author": 'Marcus Aurelius',
        "mood": 'freedom',
    },
    {
        "text": 'Unscrew the locks from the doors! Unscrew the doors themselves from their jambs!',
        "author": 'Walt Whitman',
        "mood": 'freedom',
    },
    {
        "text": 'I too am not a bit tamed, I too am untranslatable, I sound my barbaric yawp over the roofs of the world.',
        "author": 'Walt Whitman',
        "mood": 'freedom',
    },
    {
        "text": 'Reduce thyself almost to the state of a private man, and yet for all that not to become the more base and remiss in those public matters and affairs.',
        "author": 'Marcus Aurelius',
        "mood": 'freedom',
    },
    {
        "text": 'Twenty-eight years of womanly life and all so lonesome.',
        "author": 'Walt Whitman',
        "mood": 'grief',
    },
    {
        "text": 'Hope is the thing with feathers that perches in the soul, and sings the tune without the words, and never stops at all.',
        "author": 'Emily Dickinson',
        "mood": 'grief',
    },
    {
        "text": 'My mother was to die young, yet she lived with me all her latter years.',
        "author": 'Marcus Aurelius',
        "mood": 'grief',
    },
    {
        "text": 'I am the hounded slave, I wince at the bite of the dogs, hell and despair are upon me.',
        "author": 'Walt Whitman',
        "mood": 'grief',
    },
    {
        "text": 'Whatsoever doth happen in the world, doth happen justly, and so if thou dost well take heed, thou shalt find it.',
        "author": 'Marcus Aurelius',
        "mood": 'acceptance',
    },
    {
        "text": 'All things that happen unto him to embrace contentedly, as coming from Him from whom he himself also came.',
        "author": 'Marcus Aurelius',
        "mood": 'acceptance',
    },
    {
        "text": 'With all meekness and a calm cheerfulness, to expect death, as being nothing else but the resolution of those elements, of which every creature is composed.',
        "author": 'Marcus Aurelius',
        "mood": 'acceptance',
    },
    {
        "text": 'Hath anything happened unto thee? It is well, whatsoever it be.',
        "author": 'Marcus Aurelius',
        "mood": 'acceptance',
    },
    {
        "text": 'The best kind of revenge is, not to become like unto them.',
        "author": 'Marcus Aurelius',
        "mood": 'forgiveness',
    },
    {
        "text": 'Doth any man offend? It is against himself that he doth offend: why should it trouble thee?',
        "author": 'Marcus Aurelius',
        "mood": 'forgiveness',
    },
    {
        "text": 'Conceit no such things, as he that wrongeth thee conceiveth, or would have thee to conceive, but look into the matter itself, and see what it is in very truth.',
        "author": 'Marcus Aurelius',
        "mood": 'forgiveness',
    },
    {
        "text": 'Easy to be reconciled, and well pleased again with them that had offended me, as soon as any of them would be content to seek unto me again.',
        "author": 'Marcus Aurelius',
        "mood": 'forgiveness',
    },
    {
        "text": 'Hope is the thing with feathers that perches in the soul, and sings the tune without the words, and never stops at all, and sweetest in the gale is heard.',
        "author": 'Emily Dickinson',
        "mood": 'hope',
    },
    {
        "text": "I've heard it in the chillest land, and on the strangest sea; yet, never, in extremity, it asked a crumb of me.",
        "author": 'Emily Dickinson',
        "mood": 'hope',
    },
    {
        "text": 'And sore must be the storm that could abash the little bird that kept so many warm.',
        "author": 'Emily Dickinson',
        "mood": 'hope',
    },
    {
        "text": 'Sleep, I and they keep guard all night, not doubt, not decease shall dare to lay finger upon you.',
        "author": 'Walt Whitman',
        "mood": 'hope',
    },
    {
        "text": 'Consider how man, and by what part of his, is joined unto God, and how that part of man is affected, when it is said to be diffused.',
        "author": 'Marcus Aurelius',
        "mood": 'reflecting',
    },
    {
        "text": 'What is this, that now my fancy is set upon? of what things doth it consist? how long can it last?',
        "author": 'Marcus Aurelius',
        "mood": 'reflecting',
    },
    {
        "text": 'I have heard what the talkers were talking, the talk of the beginning and the end, but I do not talk of the beginning or the end.',
        "author": 'Walt Whitman',
        "mood": 'reflecting',
    },
    {
        "text": "Have you reckon'd a thousand acres much? have you reckon'd the earth much?",
        "author": 'Walt Whitman',
        "mood": 'reflecting',
    },
    {
        "text": 'Shoulder your duds dear son, and I will mine, and let us hasten forth, wonderful cities and free nations we shall fetch as we go.',
        "author": 'Walt Whitman',
        "mood": 'inspirational',
    },
    {
        "text": 'I lead no man to a dinner-table, library, exchange, but each man and each woman of you I lead upon a knoll.',
        "author": 'Walt Whitman',
        "mood": 'inspirational',
    },
    {
        "text": 'Not I, not any one else can travel that road for you, you must travel it for yourself.',
        "author": 'Walt Whitman',
        "mood": 'inspirational',
    },
    {
        "text": 'I am the teacher of athletes, he that by me spreads a wider breast than my own proves the width of my own.',
        "author": 'Walt Whitman',
        "mood": 'inspirational',
    },
    {
        "text": 'Apart from the pulling and hauling stands what I am, stands amused, complacent, compassionating, idle, unitary.',
        "author": 'Walt Whitman',
        "mood": 'reflective',
    },
    {
        "text": 'Both in and out of the game and watching and wondering at it.',
        "author": 'Walt Whitman',
        "mood": 'reflective',
    },
    {
        "text": 'I believe in you my soul, the other I am must not abase itself to you, and you must not be abased to the other.',
        "author": 'Walt Whitman',
        "mood": 'reflective',
    },
    {
        "text": 'Now I will do nothing but listen, to accrue what I hear into this song, to let sounds contribute toward it.',
        "author": 'Walt Whitman',
        "mood": 'reflective',
    },
    {
        "text": 'Now the New Year reviving old Desires, the thoughtful Soul to Solitude retires.',
        "author": 'Omar Khayyam',
        "mood": 'hopeful',
    },
    {
        "text": 'But still a Ruby kindles in the Vine, and many a Garden by the Water blows.',
        "author": 'Omar Khayyam',
        "mood": 'hopeful',
    },
    {
        "text": 'When You and I behind the Veil are past, oh, but the long, long while the World shall last.',
        "author": 'Omar Khayyam',
        "mood": 'hopeful',
    },
    {
        "text": 'Old age superbly rising! O welcome, ineffable grace of dying days!',
        "author": 'Walt Whitman',
        "mood": 'hopeful',
    },
    {
        "text": "I dilate you with tremendous breath, I buoy you up, every room of the house do I fill with an arm'd force.",
        "author": 'Walt Whitman',
        "mood": 'uplifting',
    },
    {
        "text": 'By God, you shall not go down! hang your whole weight upon me.',
        "author": 'Walt Whitman',
        "mood": 'uplifting',
    },
    {
        "text": "Long enough have you dream'd contemptible dreams, now I wash the gum from your eyes.",
        "author": 'Walt Whitman',
        "mood": 'uplifting',
    },
    {
        "text": 'I will not have a single person slighted or left away.',
        "author": 'Walt Whitman',
        "mood": 'uplifting',
    },
    {
        "text": 'The spotted hawk swoops by and accuses me, he complains of my gab and my loitering.',
        "author": 'Walt Whitman',
        "mood": 'humorous',
    },
    {
        "text": 'If you want me again look for me under your boot-soles.',
        "author": 'Walt Whitman',
        "mood": 'humorous',
    },
    {
        "text": 'Do you guess I have some intricate purpose? Well I have, for the Fourth-month showers have, and the mica on the side of a rock has.',
        "author": 'Walt Whitman',
        "mood": 'humorous',
    },
    {
        "text": 'Within ten days, if so happen, thou shalt be esteemed a god of them, who now if thou shalt return to the dogmata and to the honouring of reason, will esteem of thee no better than of a mere brute, and of an ape.',
        "author": 'Marcus Aurelius',
        "mood": 'humorous',
    },
    {
        "text": 'Death hangs over thee: whilst yet thou livest, whilst thou mayest, be good.',
        "author": 'Marcus Aurelius',
        "mood": 'mortality',
    },
    {
        "text": 'In the faces of men and women I see God, and in my own face in the glass.',
        "author": 'Walt Whitman',
        "mood": 'wonder',
    },
    {
        "text": "It is right it should be so; Man was made for Joy and Woe; and when this we rightly know thro' the World we safely go.",
        "author": 'William Blake',
        "mood": 'joy',
    },
    {
        "text": "He who shall hurt the little Wren shall never be belov'd by men.",
        "author": 'William Blake',
        "mood": 'compassion',
    },

    {
        "text": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "topics": ["work", "passion", "success"],
        "mood": "motivational",
        "length": "short",
    },
      {
        "text": "to ascend is human to fall is also human.",
        "author": "mxtx",
        "topics": ["work", "passion", "success"],
        "mood": "reflecting",
        "length": "short",
    },
      {
        "text": "I am forever your most devoted believer.",
        "author": "mxtx",
        "topics": ["work", "passion", "success"],
        "mood": "love",
        "length": "short",
    },
         {
        "text": "You've always been the strongest. But you don't need to be strong every waking moment of every day..",
        "author": "mxtx",
        "topics": ["work", "passion", "success"],
        "mood": "reflecting",
        "length": "short",
    },
        {
        "text": "Relationship should depend on chances and whether we are on the same wavelength, not on identity. If I like you, you can be a beggar and I will still like you. If I dislike you, you can be an emperor and I will still dislike you.",
        "author": "mxtx",
        "topics": ["work", "passion", "success"],
        "mood": "reflecting",
        "length": "short",
    },
     {
        "text": "I am forever your most devoted believer.",
        "author": "mxtx",
        "topics": ["work", "passion", "success"],
        "mood": "love",
        "length": "short",
    }, {
        "text": "I am forever your most devoted believer.",
        "author": "mxtx",
        "topics": ["work", "passion", "success"],
        "mood": "love",
        "length": "short",
    }, 
    {
        "text": "In the middle of every difficulty lies opportunity.",
        "author": "Albert Einstein",
        "topics": ["difficulty", "opportunity", "resilience"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Imagination is more important than knowledge.",
        "author": "Albert Einstein",
        "topics": ["imagination", "creativity", "knowledge"],
        "mood": "inspirational",
        "length": "short",
    },
    {
        "text": "Life is what happens when you're busy making other plans.",
        "author": "John Lennon",
        "topics": ["life", "plans", "mindfulness"],
        "mood": "reflective",
        "length": "short",
    },
    {
        "text": "The future belongs to those who believe in the beauty of their dreams.",
        "author": "Eleanor Roosevelt",
        "topics": ["future", "dreams", "belief"],
        "mood": "motivational",
        "length": "medium",
    },
    {
        "text": "It is during our darkest moments that we must focus to see the light.",
        "author": "Aristotle",
        "topics": ["darkness", "hope", "resilience", "focus"],
        "mood": "hopeful",
        "length": "medium",
    },
    {
        "text": "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
        "author": "Mother Teresa",
        "topics": ["love", "kindness", "happiness"],
        "mood": "uplifting",
        "length": "medium",
    },
    {
        "text": "When you reach the end of your rope, tie a knot in it and hang on.",
        "author": "Franklin D. Roosevelt",
        "topics": ["perseverance", "strength", "resilience"],
        "mood": "motivational",
        "length": "medium",
    },
    {
        "text": "Always remember that you are absolutely unique. Just like everyone else.",
        "author": "Margaret Mead",
        "topics": ["uniqueness", "identity", "humor"],
        "mood": "humorous",
        "length": "short",
    },
    {
        "text": "Do not go where the path may lead, go instead where there is no path and leave a trail.",
        "author": "Ralph Waldo Emerson",
        "topics": ["leadership", "courage", "independence"],
        "mood": "inspirational",
        "length": "medium",
    },
    {
        "text": "You will face many defeats in life, but never let yourself be defeated.",
        "author": "Maya Angelou",
        "topics": ["defeat", "resilience", "strength"],
        "mood": "motivational",
        "length": "medium",
    },
    {
        "text": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "author": "Nelson Mandela",
        "topics": ["resilience", "glory", "perseverance"],
        "mood": "inspirational",
        "length": "long",
    },
    {
        "text": "In the end, it's not the years in your life that count. It's the life in your years.",
        "author": "Abraham Lincoln",
        "topics": ["life", "meaning", "time"],
        "mood": "reflective",
        "length": "medium",
    },
    {
        "text": "Never let the fear of striking out keep you from playing the game.",
        "author": "Babe Ruth",
        "topics": ["fear", "courage", "action"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Life is either a daring adventure or nothing at all.",
        "author": "Helen Keller",
        "topics": ["life", "adventure", "courage"],
        "mood": "inspirational",
        "length": "short",
    },
    {
        "text": "Many of life's failures are people who did not realize how close they were to success when they gave up.",
        "author": "Thomas Edison",
        "topics": ["failure", "success", "perseverance"],
        "mood": "motivational",
        "length": "long",
    },
    {
        "text": "You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose.",
        "author": "Dr. Seuss",
        "topics": ["choices", "independence", "potential"],
        "mood": "uplifting",
        "length": "long",
    },
    {
        "text": "If life were predictable it would cease to be life, and be without flavor.",
        "author": "Eleanor Roosevelt",
        "topics": ["life", "unpredictability", "adventure"],
        "mood": "reflective",
        "length": "short",
    },
    {
        "text": "If you look at what you have in life, you'll always have more.",
        "author": "Oprah Winfrey",
        "topics": ["gratitude", "abundance", "mindfulness"],
        "mood": "uplifting",
        "length": "short",
    },
    {
        "text": "Two roads diverged in a wood, and I took the one less traveled by, and that has made all the difference.",
        "author": "Robert Frost",
        "topics": ["choices", "individuality", "courage"],
        "mood": "reflective",
        "length": "long",
    },
    {
        "text": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
        "topics": ["perseverance", "progress", "patience"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.",
        "author": "Thomas Edison",
        "topics": ["weakness", "success", "persistence"],
        "mood": "motivational",
        "length": "long",
    },
    {
        "text": "You miss 100% of the shots you don't take.",
        "author": "Wayne Gretzky",
        "topics": ["action", "opportunity", "courage"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "Whether you think you can or you think you can't, you're right.",
        "author": "Henry Ford",
        "topics": ["mindset", "belief", "success"],
        "mood": "motivational",
        "length": "short",
    },
    {
        "text": "I have learned over the years that when one's mind is made up, this diminishes fear.",
        "author": "Rosa Parks",
        "topics": ["courage", "fear", "determination"],
        "mood": "inspirational",
        "length": "medium",
    },
    {
        "text": "I alone cannot change the world, but I can cast a stone across the waters to create many ripples.",
        "author": "Mother Teresa",
        "topics": ["change", "impact", "hope"],
        "mood": "hopeful",
        "length": "medium",
    },
    {
        "text": "No act of kindness, no matter how small, is ever wasted.",
        "author": "Aesop",
        "topics": ["kindness", "generosity", "impact"],
        "mood": "uplifting",
        "length": "short",
    },
    {
        "text": "We know what we are, but know not what we may be.",
        "author": "William Shakespeare",
        "topics": ["potential", "identity", "philosophy"],
        "mood": "reflective",
        "length": "short",
    },
    {
        "text": "Good friends, good books, and a sleepy conscience: this is the ideal life.",
        "author": "Mark Twain",
        "topics": ["friendship", "books", "happiness", "humor"],
        "mood": "humorous",
        "length": "short",
    },
    {
        "text": "Happiness is not something ready made. It comes from your own actions.",
        "author": "Dalai Lama",
        "topics": ["happiness", "action", "mindfulness"],
        "mood": "uplifting",
        "length": "short",
    },
]

# All unique values — useful for building intent classifiers
ALL_MOODS   = sorted({q["mood"]   for q in QUOTES})
#ALL_TOPICS  = sorted({t           for q in QUOTES for t in q["topics"]})
ALL_AUTHORS = sorted({q["author"] for q in QUOTES})

if __name__ == "__main__":
    print(f"Total quotes : {len(QUOTES)}")
    print(f"Moods        : {ALL_MOODS}")
    #print(f"Unique topics: {len(ALL_TOPICS)}")
    print(f"Authors      : {len(ALL_AUTHORS)}")
