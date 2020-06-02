import os
import shutil

def run_ingest():
	'''
		Obtains 2K training images (1000 dogs, 1000 cats)
		1K validation images (500 dogs, 500 cats)
		1K test images (500 dogs, 500 cats)
	'''
	HOME_DIR = os.path.dirname(os.path.abspath('__FILE__'))
	WORKSPACE_DIR = os.path.join(HOME_DIR, 'workspace')
	DATASOURCE_DIR = os.path.join(WORKSPACE_DIR, 'PetImages')
	CATS_DIR = os.path.join(DATASOURCE_DIR, 'Cat')
	DOGS_DIR = os.path.join(DATASOURCE_DIR, 'Dog')

	# Read
	cats_imgs = [di for di in os.listdir(CATS_DIR) if di.endswith('.jpg')]
	dogs_imgs = [di for di in os.listdir(DOGS_DIR) if di.endswith('.jpg')]

	# Make directories for all 
	split_dirs = ('train', 'validation', 'test')
	cat_dirs = ('cat', 'dog')
		
	for split_dir in split_dirs:
		try:
			os.mkdir(os.path.join(WORKSPACE_DIR, split_dir))
		except FileExistsError:
			pass
		for cat_dir in cat_dirs:
			try:
				os.mkdir(os.path.join(WORKSPACE_DIR, split_dir, cat_dir))
			except FileExistsError:
				pass

	# Copy
	TRAIN_TOTAL, VAL_TOTAL, TEST_TOTAL = 1000, 500, 500
	train_count, val_count, test_count = 0, 0, 0
	for (c, d) in zip(cats_imgs, dogs_imgs):
		if train_count < TRAIN_TOTAL:
			cats_target_dir = os.path.join(WORKSPACE_DIR, split_dirs[0], cat_dirs[0])
			dogs_target_dir = os.path.join(WORKSPACE_DIR, split_dirs[0], cat_dirs[1])

			cats_src = os.path.join(CATS_DIR,c)
			dogs_src = os.path.join(DOGS_DIR,d)
			cats_tgt = os.path.join(cats_target_dir,c) 
			dogs_tgt = os.path.join(dogs_target_dir,d)
			shutil.copyfile(cats_src, cats_tgt)
			shutil.copyfile(dogs_src, dogs_tgt)

			train_count +=1
		
		elif val_count < VAL_TOTAL:
			cats_target_dir = os.path.join(WORKSPACE_DIR, split_dirs[1], cat_dirs[0])
			dogs_target_dir = os.path.join(WORKSPACE_DIR, split_dirs[1], cat_dirs[1])

			cats_src = os.path.join(CATS_DIR,c)
			dogs_src = os.path.join(DOGS_DIR,d)
			cats_tgt = os.path.join(cats_target_dir,c) 
			dogs_tgt = os.path.join(dogs_target_dir,d)
			shutil.copyfile(cats_src, cats_tgt)
			shutil.copyfile(dogs_src, dogs_tgt)
			val_count +=1

		elif test_count < TEST_TOTAL:
			cats_target_dir = os.path.join(WORKSPACE_DIR, split_dirs[2], cat_dirs[0])
			dogs_target_dir = os.path.join(WORKSPACE_DIR, split_dirs[2], cat_dirs[1])

			cats_src = os.path.join(CATS_DIR,c)
			dogs_src = os.path.join(DOGS_DIR,d)
			cats_tgt = os.path.join(cats_target_dir,c) 
			dogs_tgt = os.path.join(dogs_target_dir,d)
			shutil.copyfile(cats_src, cats_tgt)
			shutil.copyfile(dogs_src, dogs_tgt)
			test_count +=1
		else:
			break

	return True