#!/usr/bin/python

from gimpfu import *

def plugin_main(timg, tdrawable, g_radius = 10.0, replace_original = False):
    print "Hello! You run smooth fix plugin made by Andrei Ermicioi (erani.mail@gmail.com)"
    default_layer = pdb.gimp_image_get_active_layer(timg)
    
    blur_layer = pdb.gimp_layer_copy(default_layer, True)
    pdb.gimp_image_insert_layer(timg, blur_layer, None, -1)
    pdb.plug_in_gauss_rle2(timg, blur_layer, g_radius, g_radius)
    
    grain_layer = pdb.gimp_layer_copy(default_layer, True)
    pdb.gimp_image_insert_layer(timg, grain_layer, None, -1)
    pdb.gimp_image_set_active_layer(timg, grain_layer)
    pdb.gimp_layer_set_mode(grain_layer, 20)    
    vlayer = pdb.gimp_layer_new_from_visible(timg, timg, "visible") 
    pdb.gimp_image_insert_layer(timg, vlayer, None, -1)
    grain_layer = pdb.gimp_image_merge_down(timg, vlayer, 0)
    pdb.gimp_layer_set_mode(grain_layer, 20)
    pdb.gimp_desaturate(grain_layer)
    
    grain_layer2 = pdb.gimp_layer_copy(grain_layer, True)
    pdb.gimp_image_insert_layer(timg, grain_layer2, None, -1)
    pdb.gimp_desaturate(grain_layer2)
    
    if replace_original:
		timg.flatten()
		filename = pdb.gimp_image_get_filename(timg)
		print "Saving over original"
		print filename
		pdb.gimp_file_save(timg, timg.active_layer, filename, timg.name)
	
register(
    "python_fu_resize",
    "The plugin try to fix the smooth of the image.",
    "The plugin try to fix the smooth of the image.",
    "Andrei Ermicioi (erani.mail@gmail.com)",
    "Andrei Ermicioi (erani.mail@gmail.com)",
    "08 May 2013",
    "<Image>/Filters/SmoothFix",
	"RGB*, GRAY*",
	[
	(PF_FLOAT, "g_radius", "Smooth radius", 10),
	(PF_BOOL, "replace_original", "Replace original", False)],
	[],
	plugin_main)

main()
