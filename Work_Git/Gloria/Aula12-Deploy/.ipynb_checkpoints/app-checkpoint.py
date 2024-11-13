{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6e03987-76ba-4c36-8616-c7de7cf6a1be",
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash\n",
    "from dash import html\n",
    "\n",
    "app = dash.Dash(__name__)\n",
    "\n",
    "app.layout = html.Div(\"Hello, Dash!\")\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
