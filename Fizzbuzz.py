{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM5Oxsc+PTf5r5lRQLIvm4o",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mlambert05/CSCI2003/blob/main/Fizzbuzz_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5jeBpZLmKWHL",
        "outputId": "c9b80b6c-0b1c-4949-b3f4-18892651fe9d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Give me a number 15\n",
            "FizzBuzz\n"
          ]
        }
      ],
      "source": [
        "guess = int(input(\"Give me a number \"))\n",
        "\n",
        "three = (guess) % 3\n",
        "\n",
        "five= (guess) % 5\n",
        "\n",
        "if (three) == 0 and (five) == 0:\n",
        "  print(\"FizzBuzz\")\n",
        "\n",
        "elif (three) == 0:\n",
        "  print(\"fizz\")\n",
        "\n",
        "elif (five) == 0:\n",
        "  print(\"buzz\")"
      ]
    }
  ]
}
