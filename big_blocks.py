# this is a script that will find the 100x100 pixel blocks that have the greatest concentration of green pixels

import handle_image as hi

# first, load our awesome image
img = hi.load_image("dog.png")

# next, we compute our green difference with red and blue, and then add them together
g_r_diff = hi.channel_diff(img, 1, 0)
g_b_diff = hi.channel_diff(img, 1, 2)

g_diff = g_r_diff + g_b_diff

# now we can compute the integral image of our g_diff
intg = hi.integral_img(g_diff)

# finally, we need to loop over our intg image and check for which 100x100 block is the most green.
# TODO: we haven't implemented this yet