{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyODOYjgnboppo4oMepuVsSO",
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
        "<a href=\"https://colab.research.google.com/github/mlambert05/CSCI2003/blob/main/lyric_analyzer.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "text = \"The FitnessGram Pacer test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter Pacer test will begin in 30 seconds. Line up at the start. The running speed starts slowly, but gets faster each minute after you hear this signal *boop*. A single lap should be completed each time you hear this sound *ding*. Remember to run in a straight line, and run as long as possible. The second time you fail to complete a lap before the sound, your test is over. The test will begin on the word start. On your mark, get ready, start.\"\n",
        "\n",
        "print(text.split( ))\n",
        "\n",
        "word_count = {}\n",
        "\n",
        "for word in text.split():\n",
        "  if word in word_count:\n",
        "   word_count [word] += 1\n",
        "\n",
        "  else:\n",
        "    word_count [word] = 1\n",
        "\n",
        "print(word_count)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GJYtXEWg53xp",
        "outputId": "0db5bc16-e812-4052-8f12-2250bb85e153"
      },
      "execution_count": 116,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['The', 'FitnessGram', 'Pacer', 'test', 'is', 'a', 'multistage', 'aerobic', 'capacity', 'test', 'that', 'progressively', 'gets', 'more', 'difficult', 'as', 'it', 'continues.', 'The', '20', 'meter', 'Pacer', 'test', 'will', 'begin', 'in', '30', 'seconds.', 'Line', 'up', 'at', 'the', 'start.', 'The', 'running', 'speed', 'starts', 'slowly,', 'but', 'gets', 'faster', 'each', 'minute', 'after', 'you', 'hear', 'this', 'signal', '*boop*.', 'A', 'single', 'lap', 'should', 'be', 'completed', 'each', 'time', 'you', 'hear', 'this', 'sound', '*ding*.', 'Remember', 'to', 'run', 'in', 'a', 'straight', 'line,', 'and', 'run', 'as', 'long', 'as', 'possible.', 'The', 'second', 'time', 'you', 'fail', 'to', 'complete', 'a', 'lap', 'before', 'the', 'sound,', 'your', 'test', 'is', 'over.', 'The', 'test', 'will', 'begin', 'on', 'the', 'word', 'start.', 'On', 'your', 'mark,', 'get', 'ready,', 'start.']\n",
            "{'The': 5, 'FitnessGram': 1, 'Pacer': 2, 'test': 5, 'is': 2, 'a': 3, 'multistage': 1, 'aerobic': 1, 'capacity': 1, 'that': 1, 'progressively': 1, 'gets': 2, 'more': 1, 'difficult': 1, 'as': 3, 'it': 1, 'continues.': 1, '20': 1, 'meter': 1, 'will': 2, 'begin': 2, 'in': 2, '30': 1, 'seconds.': 1, 'Line': 1, 'up': 1, 'at': 1, 'the': 3, 'start.': 3, 'running': 1, 'speed': 1, 'starts': 1, 'slowly,': 1, 'but': 1, 'faster': 1, 'each': 2, 'minute': 1, 'after': 1, 'you': 3, 'hear': 2, 'this': 2, 'signal': 1, '*boop*.': 1, 'A': 1, 'single': 1, 'lap': 2, 'should': 1, 'be': 1, 'completed': 1, 'time': 2, 'sound': 1, '*ding*.': 1, 'Remember': 1, 'to': 2, 'run': 2, 'straight': 1, 'line,': 1, 'and': 1, 'long': 1, 'possible.': 1, 'second': 1, 'fail': 1, 'complete': 1, 'before': 1, 'sound,': 1, 'your': 2, 'over.': 1, 'on': 1, 'word': 1, 'On': 1, 'mark,': 1, 'get': 1, 'ready,': 1}\n"
          ]
        }
      ]
    }
  ]
}