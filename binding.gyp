{
  'targets': [
    {
      'target_name': 'bigint',
      'sources': [ 'bigint.cc' ],
      'conditions': [
        ['OS=="linux"',
          {
            'include_dirs': [
              '/tmp/gmp513ubuntu/include',
            ],
            'link_settings': {
              'libraries': [
                '-lgmp', '-L/tmp/gmp513ubuntu/lib'
              ]
            }
          }
        ],
        ['OS=="mac"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp'
              ]
            }
          }
        ],
        ['OS=="win"',
          {
            'link_settings': {
              'libraries': [
                '-lgmp.lib'
              ],
            }
          }
        ]
      ]
    }
  ]
}
