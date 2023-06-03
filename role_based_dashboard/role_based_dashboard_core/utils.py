import random
import string

from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# To create slug url
def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



def order_tracking_id_generator_signal(sender, instance, *args, **kwargs):
    if not instance.tracking_number:
        instance.tracking_number = unique_slug_generator(instance)



def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = "slug" + str(random.randint(0,10000)) + random_string_generator(size = 4)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug = slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_string_generator(size = 4))
        return unique_slug_generator(instance, new_slug = new_slug)
    return slug