from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from lua_server.core.models.helpers.identifier import make_identifier
from rest_framework.authtoken.models import Token


LANGUAGES = (
    # Top languages put on top. The locations for these languages are properly marked.

    ("pt", "Português"),
    ("fr", "Français"),
    ('en', 'English'),
    ("es", "Español"),

    ("ab", "Abkhazian"),
    ("aa", "Afar"),
    ("af", "Afrikaans"),
    ("sq", "Albanian"),
    ("am", "Amharic"),
    ("ar", "Arabic"),
    ("an", "Aragonese"),
    ("hy", "Armenian"),
    ("as", "Assamese"),
    ("ae", "Avestan"),
    ("ay", "Aymara"),
    ("az", "Azerbaijani"),
    ("ba", "Bashkir"),
    ("eu", "Basque"),
    ("be", "Belarusian"),
    ("bn", "Bengali"),
    ("bh", "Bihari"),
    ("bi", "Bislama"),
    ("bs", "Bosnian"),
    ("br", "Breton"),
    ("bg", "Bulgarian"),
    ("my", "Burmese"),
    ("ca", "Catalan"),
    ("ch", "Chamorro"),
    ("ce", "Chechen"),
    ("zh", "Chinese"),
    ("cu", "Church/Slavic/Slavonic"),
    ("cv", "Chuvash"),
    ("kw", "Cornish"),
    ("co", "Corsican"),
    ("hr", "Croatian"),
    ("cs", "Czech"),
    ("da", "Danish"),
    ("dv", "Divehi/Dhivehi/Maldivian"),
    ("nl", "Dutch"),
    ("dz", "Dzongkha"),

    # English fits here...

    ("eo", "Esperanto"),
    ("et", "Estonian"),
    ("fo", "Faroese"),
    ("fj", "Fijian"),
    ("fi", "Finnish"),

    # French fits here...

    ("gd", "Gaelic (Scottish)"),
    ("gl", "Galician"),
    ("ka", "Georgian"),
    ("de", "German"),
    ("el", "Greek"),
    ("gn", "Guarani"),
    ("gu", "Gujarati"),
    ("ht", "Haitian Creole"),
    ("ha", "Hausa"),
    ("he", "Hebrew"),
    ("hz", "Herero"),
    ("hi", "Hindi"),
    ("ho", "Hiri/Motu"),
    ("hu", "Hungarian"),
    ("is", "Icelandic"),
    ("io", "Ido"),
    ("id", "Indonesian"),
    ("ia", "Interlingua"),
    ("ie", "Interlingue"),
    ("iu", "Inuktitut"),
    ("ik", "Inupiaq"),
    ("ga", "Irish"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("jv", "Javanese"),
    ("kl", "Kalaallisut"),
    ("kn", "Kannada"),
    ("ks", "Kashmiri"),
    ("kk", "Kazakh"),
    ("km", "Khmer"),
    ("ki", "Kikuyu/Gikuyu"),
    ("rw", "Kinyarwanda"),
    ("ky", "Kirghiz"),
    ("kv", "Komi"),
    ("ko", "Korean"),
    ("kj", "Kuanyama/Kwanyama"),
    ("ku", "Kurdish"),
    ("lo", "Lao"),
    ("la", "Latin"),
    ("lv", "Latvian"),
    ("li", "Limburgan/Limburger/Limburgish"),
    ("ln", "Lingala"),
    ("lt", "Lithuanian"),
    ("lb", "Luxembourgish/Letzeburgesch"),
    ("mk", "Macedonian"),
    ("mg", "Malagasy"),
    ("ms", "Malay"),
    ("ml", "Malayalam"),
    ("mt", "Maltese"),
    ("gv", "Manx"),
    ("mi", "Maori"),
    ("mr", "Marathi"),
    ("mh", "Marshallese"),
    ("mo", "Moldavian"),
    ("mn", "Mongolian"),
    ("na", "Nauru"),
    ("nv", "Navaho/Navajo"),
    ("nd", "Ndebele/North"),
    ("nr", "Ndebele/South"),
    ("ng", "Ndonga"),
    ("ne", "Nepali"),
    ("se", "Northern/Sami"),
    ("no", "Norwegian"),
    ("nb", "Norwegian/Bokmal"),
    ("nn", "Norwegian/Nynorsk"),
    ("ny", "Nyanja/Chichewa/Chewa"),
    ("oc", "Occitan/Provencal"),
    ("or", "Oriya"),
    ("om", "Oromo"),
    ("os", "Ossetian/Ossetic"),
    ("pi", "Pali"),
    ("pa", "Panjabi"),
    ("fa", "Persian"),
    ("pl", "Polish"),

    # Portuguese fits here...

    ("ps", "Pushto"),
    ("qu", "Quechua"),
    ("rm", "Raeto-Romance"),
    ("ro", "Romanian"),
    ("rn", "Rundi"),
    ("ru", "Russian"),
    ("sm", "Samoan"),
    ("sg", "Sango"),
    ("sa", "Sanskrit"),
    ("sc", "Sardinian"),
    ("sr", "Serbian"),
    ("sn", "Shona"),
    ("ii", "Sichuan"),
    ("sd", "Sindhi"),
    ("si", "Sinhala/Sinhalese"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("so", "Somali"),
    ("st", "Sotho/Southern"),

    # Spanish fits here...

    ("su", "Sundanese"),
    ("sw", "Swahili"),
    ("ss", "Swati"),
    ("sv", "Swedish"),
    ("tl", "Tagalog"),
    ("ty", "Tahitian"),
    ("tg", "Tajik"),
    ("ta", "Tamil"),
    ("tt", "Tatar"),
    ("te", "Telugu"),
    ("th", "Thai"),
    ("bo", "Tibetan"),
    ("ti", "Tigrinya"),
    ("to", "Tonga"),
    ("ts", "Tsonga"),
    ("tn", "Tswana"),
    ("tr", "Turkish"),
    ("tk", "Turkmen"),
    ("tw", "Twi"),
    ("ug", "Uighur"),
    ("uk", "Ukrainian"),
    ("ur", "Urdu"),
    ("uz", "Uzbek"),
    ("vi", "Vietnamese"),
    ("vo", "Volapuk"),
    ("wa", "Walloon"),
    ("cy", "Welsh"),
    ("fy", "Western/Frisian"),
    ("wo", "Wolof"),
    ("xh", "Xhosa"),
    ("yi", "Yiddish"),
    ("yo", "Yoruba"),
    ("za", "Zhuang/Chuang"),
    ("zu", "Zulu"),
)


class User(AbstractUser):
    id = models.BigIntegerField(primary_key=True, editable=False)
    profile_picture = CloudinaryField('image', blank=True)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user_id=self.id)
    
    def __str__(self):
        return self.username
