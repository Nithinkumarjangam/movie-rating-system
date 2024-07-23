import tkinter as tk
from tkinter import messagebox

class MovieRatingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Rating App")

        self.ratings = {}

        self.create_widgets()

    def create_widgets(self):
        self.movie_name_label = tk.Label(self.master, text="Movie Name:")
        self.movie_name_label.grid(row=0, column=0, padx=10, pady=10)

        self.movie_name_entry = tk.Entry(self.master)
        self.movie_name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.rating_label = tk.Label(self.master, text="Rating (1-5):")
        self.rating_label.grid(row=1, column=0, padx=10, pady=10)

        self.rating_scale = tk.Scale(self.master, from_=1, to=5, orient=tk.HORIZONTAL)
        self.rating_scale.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(self.master, text="Add Rating", command=self.add_rating)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.average_button = tk.Button(self.master, text="Average Rating", command=self.show_average_rating)
        self.average_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.display_button = tk.Button(self.master, text="Display Ratings", command=self.display_ratings)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.bar_chart_canvas = tk.Canvas(self.master, width=400, height=200)
        self.bar_chart_canvas.grid(row=5, column=0, columnspan=2, pady=10)

    def add_rating(self):
        movie_name = self.movie_name_entry.get()
        rating = self.rating_scale.get()

        if movie_name:
            self.ratings[movie_name] = rating
            messagebox.showinfo("Success", f"Added rating for {movie_name}: {rating}")
        else:
            messagebox.showwarning("Input Error", "Please enter a movie name.")

    def show_average_rating(self):
        if self.ratings:
            average_rating = sum(self.ratings.values()) / len(self.ratings)
            messagebox.showinfo("Average Rating", f"The average rating is: {average_rating:.2f}")
        else:
            messagebox.showwarning("No Ratings", "No ratings available to calculate the average.")

    def display_ratings(self):
        self.bar_chart_canvas.delete("all")

        if self.ratings:
            max_height = 150
            bar_width = 30
            spacing = 10
            x = spacing

            for movie, rating in self.ratings.items():
                bar_height = (rating / 5) * max_height
                self.bar_chart_canvas.create_rectangle(x, max_height - bar_height, x + bar_width, max_height, fill="blue")
                self.bar_chart_canvas.create_text(x + bar_width / 2, max_height + 10, text=movie, anchor=tk.N)
                self.bar_chart_canvas.create_text(x + bar_width / 2, max_height - bar_height - 10, text=str(rating), anchor=tk.S)
                x += bar_width + spacing
        else:
            messagebox.showwarning("No Ratings", "No ratings available to display.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MovieRatingApp(root)
    root.mainloop()
