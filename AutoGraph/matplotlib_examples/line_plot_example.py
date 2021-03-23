import matplotlib.pyplot as plt
import numpy as np

# # styling
# plt.style.use("ggplot")
# plt.style.use("fivethirtyeight")
# plt.style.use("seaborn")
# plt.xkcd()


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(
    ages_x,
    py_dev_y,
    label="Python",
    # color="#5a7d9a",
    # linewidth=3,
)

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(
    ages_x,
    js_dev_y,
    label="JavaScript",
    # color="#adad3b",
    # linewidth=3,
)

# Median Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(
    ages_x,
    dev_y,
    label="All Devs",
    color="#444444",
    linestyle="--",
)


# config
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.title("Median Salary (USD) by Age")
plt.legend()

plt.grid(True)

plt.tight_layout()  # fix formatting on smaller screens
# plt.savefig(fname="plot.png")
plt.show()
