def md_nre(y, y_hat, n, p):
    # Tính căn bậc n của y và y_hat
    y_root = y ** (1 / n)
    y_hat_root = y_hat ** (1 / n)
    # MD_nRE
    loss = abs(y_root - y_hat_root) ** p

    return loss


# Test
y_values = [100, 50, 20, 5.5, 1.0, 0.6]
y_hat_values = [99.5, 49.5, 19.5, 5.0, 0.5, 0.1]
n = 2
p = 1

for y, y_hat in zip(y_values, y_hat_values):
    result = md_nre(y, y_hat, n, p)
    print(f'y = {y}, y_hat = {y_hat}, MD_nRE (n={n}, p={p}) = {result:.3f}')
