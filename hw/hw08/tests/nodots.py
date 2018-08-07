test = {
  'name': 'nodots',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (nodots '(1 . 2))
          (1 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 2 . 3))
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '((1 . 2) 3))
          ((1 2) 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 (2 3 . 4) . 3))
          (1 (2 3 4) 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (nodots '(1 . ((2 3 . 4) . 3)))
          99664260ecd386c62f28106482facddd
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load 'hw08)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
