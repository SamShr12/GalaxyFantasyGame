def transform(self, x, y):
    #here render 2d and 3d
     #return self.transform_2D(x, y) #2d transfromation
    return self.transform_perspective(x, y)  # 3d transform


def transform_2D(self, x, y):
    return int(x), int(y)


def transform_perspective(self, x, y):
    # transfrom 2d to 3d
    lin_y = y * self.perspective_point_y / self.height

    if lin_y > self.perspective_point_y:
        lin_y = self.perspective_point_y

    diff_x = x - self.perspective_point_x
    diff_y = self.perspective_point_y - lin_y
    factor_y = diff_y / self.perspective_point_y
    factor_y = pow(factor_y, 4)
    tr_x = self.perspective_point_x + diff_x * factor_y
    tr_y = self.perspective_point_y - factor_y * self.perspective_point_y
    return int(tr_x), int(tr_y)

