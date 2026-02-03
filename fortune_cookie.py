{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN/mUsch+O/jP6KmVkaVNA4",
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
        "<a href=\"https://colab.research.google.com/github/mlambert05/CSCI2003/blob/main/fortune_cookie.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "lucky_number = random.randint(1,100)\n",
        "\n",
        "messgae = random.randint(1,4)\n",
        "\n",
        "if message == 1:\n",
        "  print('Today will be full of joy')\n",
        "\n",
        "if message == 2:\n",
        "  print('Keep friends close')\n",
        "\n",
        "if message == 3:\n",
        "  print('Your trials will pass')\n",
        "\n",
        "if message == 4:\n",
        "  print('Watch for a fateful encounter')\n",
        "print(f\"{messgae}, Your lucky number is {lucky_number}\")\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HhAgU0iHbESR",
        "outputId": "205f66f6-088c-4f70-f85f-44d225b02a02"
      },
      "execution_count": 118,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Your trials will pass\n",
            "4, Your lucky number is 20\n"
          ]
        }
      ]

    
