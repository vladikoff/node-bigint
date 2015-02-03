{
  'targets': [
    {
      'target_name': 'bigint',
      'sources': [ 'bigint.cc' ],
      'conditions': [
        ['OS=="linux"',
          {
            'include_dirs': [
              '/app/.heroku/vendor/include',
            ],
            'link_settings': {
              'libraries': [
                '-lgmp', '-L/app/.heroku/vendor/lib/'
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
