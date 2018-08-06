test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pokemon = {'pikachu': 25, 'dragonair': 148, 'mew': 151}
          >>> pokemon['pikachu']
          25
          >>> len(pokemon)
          3
          >>> pokemon['jolteon'] = 135
          >>> pokemon['mew'] = 25
          >>> len(pokemon)
          4
          >>> 'mewtwo' in pokemon
          False
          >>> 'pikachu' in pokemon
          True
          >>> 25 in pokemon
          False
          >>> 148 in pokemon.values()
          True
          >>> 151 in pokemon.keys()
          False
          >>> 'mew' in pokemon.keys()
          True
          >>> pokemon['ditto'] = pokemon['jolteon']
          >>> pokemon['ditto']
          135
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> letters = {'a': 1, 'b': 2, 'c': 3}
          >>> 'a' in letters
          True
          >>> 2 in letters
          False
          >>> sorted(list(letters.keys()))
          ['a', 'b', 'c']
          >>> sorted(list(letters.items()))
          8aff5a385dd3d9c4f581f980174d65c9
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> food = {'bulgogi': 10, 'falafel': 4, 'ceviche': 7}
          >>> food['ultimate'] = food['bulgogi'] + food['ceviche']
          >>> food['ultimate']
          6c4c5c2026b2b916aff21d836960bbd9
          # locked
          >>> len(food)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> food['ultimate'] += food['falafel']
          >>> food['ultimate']
          286a63c09649ab2e465e9e1abab82eba
          # locked
          >>> food['bulgogi'] = food['falafel']
          >>> len(food)
          fef77a143fa87e746554afe9ebb16a3d
          # locked
          >>> 'gogi' in food
          ac667055c8e3c84ad7260b0fefa2e007
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
