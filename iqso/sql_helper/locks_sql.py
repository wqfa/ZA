from sqlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr









def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

iqvois1 = "iqso/helpers/styles/Voic/ابو عباس لو تاكل خره.ogg"
iqvois2 = "iqso/helpers/styles/Voic/استمر نحن معك.ogg"
iqvois3 = "iqso/helpers/styles/Voic/افحط بوجه.ogg"
iqvois4 = "iqso/helpers/styles/Voic/اكعد لا اسطرك سطره العباس.ogg"
iqvois5 = "iqso/helpers/styles/Voic/اللهم لا شماته.ogg"
iqvois6 = "iqso/helpers/styles/Voic/امرع دينه.ogg"
iqvois7 = "iqso/helpers/styles/Voic/امشي بربوك.ogg"
iqvois8 = "iqso/helpers/styles/Voic/انت اسكت انت اسكت.ogg"
iqvois9 = "iqso/helpers/styles/Voic/انت سايق زربه.ogg"
iqvois10 = "iqso/helpers/styles/Voic/اوني تشان.ogg"
iqvois11 = "iqso/helpers/styles/Voic/برافو عليك استادي.ogg"
iqvois12 = "iqso/helpers/styles/Voic/بلوك محترم.ogg"
iqvois13 = "iqso/helpers/styles/Voic/بووم في منتصف الجبهة.ogg"
iqvois14 = "iqso/helpers/styles/Voic/بيتش.ogg"
iqvois15 = "iqso/helpers/styles/Voic/تخوني ؟.ogg"
iqvois15 = "iqso/helpers/styles/Voic/تره متكدرلي.ogg"
iqvois17 = "iqso/helpers/styles/Voic/تعبان اوي.ogg"
iqvois18 = "iqso/helpers/styles/Voic/تكذب.ogg"
iqvois19 = "iqso/helpers/styles/Voic/حسبي الله.ogg"
iqvois20 = "iqso/helpers/styles/Voic/حشاش.ogg"
iqvois21 = "iqso/helpers/styles/Voic/حقير.ogg"
iqvois22 = "iqso/helpers/styles/Voic/خاص.ogg"
iqvois23 = "iqso/helpers/styles/Voic/خاله ما تنامون.ogg"
iqvois24 = "iqso/helpers/styles/Voic/خرب شرفي اذا ابقى بالعراق.ogg"
iqvois25 = "iqso/helpers/styles/Voic/دكات الوكت الاغبر.ogg"
iqvois26 = "iqso/helpers/styles/Voic/ررردح.ogg"
iqvois27 = "iqso/helpers/styles/Voic/سلامن عليكم.ogg"
iqvois28 = "iqso/helpers/styles/Voic/شعليك.ogg"
iqvois29 = "iqso/helpers/styles/Voic/شكد شفت ناس مدودة.ogg"
iqvois30 = "iqso/helpers/styles/Voic/شلون ،.ogg"
iqvois31 = "iqso/helpers/styles/Voic/صح لنوم.ogg"
iqvois32 = "iqso/helpers/styles/Voic/صمت.ogg"
iqvois33 = "iqso/helpers/styles/Voic/ضحكة مصطفى الحجي.ogg"
iqvois34 = "iqso/helpers/styles/Voic/طماطه.ogg"
iqvois35 = "iqso/helpers/styles/Voic/طيح الله حضك.ogg"
iqvois36 = "iqso/helpers/styles/Voic/فاك يوو.ogg"
iqvois37 = "iqso/helpers/styles/Voic/فرحان.ogg"
iqvois38 = "iqso/helpers/styles/Voic/لا تضل تضرط.ogg"
iqvois39 = "iqso/helpers/styles/Voic/لا تقتل المتعه يا مسلم.ogg"
iqvois40 = "iqso/helpers/styles/Voic/لا مستحيل.ogg"
iqvois41 = "iqso/helpers/styles/Voic/لا والله شو عصبي.ogg"
iqvois42 = "iqso/helpers/styles/Voic/لش.ogg"
iqvois43 = "iqso/helpers/styles/Voic/لك اني شعليه.ogg"
iqvois44 = "iqso/helpers/styles/Voic/ما اشرب.ogg"
iqvois45 = "iqso/helpers/styles/Voic/مع الاسف.ogg"
iqvois46 = "iqso/helpers/styles/Voic/مقتدى.ogg"
iqvois47 = "iqso/helpers/styles/Voic/من رخصتكم.ogg"
iqvois48 = "iqso/helpers/styles/Voic/منو انت.ogg"
iqvois49 = "iqso/helpers/styles/Voic/منورني.ogg"
iqvois50 = "iqso/helpers/styles/Voic/نتلاكه بالدور الثاني.ogg"
iqvois51 = "iqso/helpers/styles/Voic/نستودعكم الله.ogg"
iqvois52 = "iqso/helpers/styles/Voic/ها شنهي.ogg"
iqvois53 = "iqso/helpers/styles/Voic/ههاي الافكار حطها.ogg"
iqvois54 = "iqso/helpers/styles/Voic/وينهم.ogg"
iqvois55 = "iqso/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois56 = "iqso/helpers/styles/Voic/اريد انام.ogg"
iqvois57 = "iqso/helpers/styles/Voic/افتحك فتح.ogg"
iqvois58 = "iqso/helpers/styles/Voic/اكل خره لدوخني.ogg"
iqvois59 = "iqso/helpers/styles/Voic/السيد شنهو السيد.ogg"
iqvois60 = "iqso/helpers/styles/Voic/زيج2.ogg"
iqvois61 = "iqso/helpers/styles/Voic/زيج لهارون.ogg"
iqvois62 = "iqso/helpers/styles/Voic/زيج الناصرية.ogg"
iqvois63 = "iqso/helpers/styles/Voic/راقبو اطفالكم.ogg"
iqvois64 = "iqso/helpers/styles/Voic/راح اموتن.ogg"
iqvois65 = "iqso/helpers/styles/Voic/ذس اس مضرطة.ogg"
iqvois66 = "iqso/helpers/styles/Voic/دروح سرسح منا.ogg"
iqvois67 = "iqso/helpers/styles/Voic/خويه ما دكوم بيه.ogg"
iqvois68 = "iqso/helpers/styles/Voic/خلصت تمسلت ديلة كافي انجب.ogg"
iqvois69 = "iqso/helpers/styles/Voic/بعدك تخاف.ogg"
iqvois70 = "iqso/helpers/styles/Voic/بسبوس.ogg"
iqvois71 = "iqso/helpers/styles/Voic/اني بتيتة كحبة.ogg"
iqvois72 = "iqso/helpers/styles/Voic/انعل ابوكم لابو اليلعب وياكم طوبة.ogg"
iqvois73 = "iqso/helpers/styles/Voic/انت شدخلك.ogg"
iqvois74 = "iqso/helpers/styles/Voic/انا ماشي بطلع.ogg"
iqvois75 = "iqso/helpers/styles/Voic/امداك وامده الخلفتك.ogg"
iqvois76 = "iqso/helpers/styles/Voic/امبيههههه.ogg"
iqvois77 = "iqso/helpers/styles/Voic/هدي بيبي.ogg"
iqvois78 = "iqso/helpers/styles/Voic/هاه صدك تحجي.ogg"
iqvois79 = "iqso/helpers/styles/Voic/مو كتلك رجعني.ogg"
iqvois80 = "iqso/helpers/styles/Voic/مامرجية منك هاية.ogg"
iqvois81 = "iqso/helpers/styles/Voic/ليش هيجي.ogg"
iqvois82 = "iqso/helpers/styles/Voic/كـــافـي.ogg"
iqvois83 = "iqso/helpers/styles/Voic/كس اخت السيد.ogg"
iqvois84 = "iqso/helpers/styles/Voic/شنو كواد ولك اني هنا.ogg"
iqvois85 = "iqso/helpers/styles/Voic/شجلبت.ogg"
iqvois86 = "iqso/helpers/styles/Voic/شبيك وجه الدبس.ogg"
iqvois87 = "iqso/helpers/styles/Voic/سييييي.ogg"
iqvois88 = "iqso/helpers/styles/Voic/زيجج1.ogg"
iqvois89 = "iqso/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois90 = "iqso/helpers/styles/Voic/ياخي اسكت اسكت.ogg"
iqvois91 = "iqso/helpers/styles/Voic/وينهم.ogg"
iqvois92 = "iqso/helpers/styles/Voic/هيلو سامر وحود.ogg"
iqvois93 = "iqso/helpers/styles/Voic/هو.ogg"
iqvois94 = "iqso/helpers/styles/Voic/ههاي الافكار حطها.ogg"

def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
