from __builtins__ import *

change_hat(Hats.Green_Hat)

check_Flag = 0


def go(x, y):
	while True:
		if get_pos_y() != y:
			move(North)
		if get_pos_x() != x:
			move(West)
		if get_pos_x() == x and get_pos_y() == y:
			break


def watering():
	if get_water() <= 0.75 and num_items(Items.Water) > 0:
		use_item(Items.Water)


def reset_pos():
	# 将无人机位置重置回起始点
	while True:
		if get_pos_y() != 0:
			move(North)
		if get_pos_x() != 0:
			move(West)
		if get_pos_x() == 0 and get_pos_y() == 0:
			break


def check_number():
	if get_pos_x() % 2 == check_Flag and get_pos_y() % 2 == check_Flag:
		return True
	else:
		return False


def plant_entitles():
	global count_times
	global plant_pumpkin_flag

	if num_items(Items.Hay) <= num_items(Items.Pumpkin) + 500 and plant_pumpkin_flag == False:
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Soil:
			till()
			plant(Entities.Grass)
		else:
			plant(Entities.Grass)


	elif num_items(Items.Wood) <= num_items(Items.Hay) + 5000 and plant_pumpkin_flag == False:
		if can_harvest():
			harvest()
		if check_number():
			Flag2 = True
		else:
			Flag2 = False

		if get_ground_type() == Grounds.Soil:
			till()
			if Flag2:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
		else:
			if Flag2:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)

	elif num_items(Items.Carrot) <= num_items(Items.Wood) + 500 and plant_pumpkin_flag == False:
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Carrot)
		else:
			plant(Entities.Carrot)
	elif num_items(Items.Pumpkin) < num_items(Items.Carrot) + 500 or plant_pumpkin_flag == True:
		if can_harvest() and get_entity_type() != Entities.Pumpkin:
			harvest()
		elif can_harvest() and (count_times==4 or count_times == 0) :
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Pumpkin)
		else:
			plant(Entities.Pumpkin)
		plant_pumpkin_flag = True


if __name__ == '__main__':
	reset_pos()  # 将无人机所在点重置
	global count_times
	global plant_pumpkin_flag

	count_times = 0
	plant_pumpkin_flag = False

	Flag = 1
	mode = East
	while True:
		Y = 0

		if plant_pumpkin_flag == True and count_times < 4:
			count_times += 1
		else:
			count_times = 0
			plant_pumpkin_flag = False

		for i in range(get_world_size()):
			X = 0
			for j in range(get_world_size()):
				watering()  # 对地块进行浇水

				plant_entitles()  # 对地块进行操作

				if X < get_world_size() - 1:
					move(mode)
					X += 1
				else:
					Flag = (Flag + 1) % 2
			move(North)

			check_Flag = (check_Flag + 1) % 2

			if Flag == 1:
				mode = East
			else:
				mode = West
			Y += 1
