<<<<<<< HEAD
epiviz.Config.SETTINGS.dataServerLocation = 'http://metaviz.cbcb.umd.edu/data/';epiviz.Config.SETTINGS.dataProviders = [['epiviz.data.EpivizApiDataProvider',"test_db","http://localhost:5000/api/",[],3,{'3': 2}],['epiviz.data.EpivizApiDataProvider',"test_db","http://localhost:5000/api/",[],3,{'3': 2}]];epiviz.Config.SETTINGS.workspacesDataProvider = sprintf('epiviz.data.WebServerDataProvider,%s,%s','workspaces_provider','http://metaviz.cbcb.umd.edu/data/main.php');
=======
// This uses the UMD server for login and user management
epiviz.Config.SETTINGS.dataServerLocation = 'http://metaviz.cbcb.umd.edu/data/';

// This sets up the UMD data server as the only data provider
epiviz.Config.SETTINGS.dataProviders = [
    [
      // fully qualified class name for the class
      'epiviz.data.EpivizApiDataProvider',

      // the name of the datasource (matching the datasource in the UI add measurements dialog)
      'msd16s',

      // where the api is located, relative to dataServerLocation (see above)
      'http://metaviz.cbcb.umd.edu/api',

      // retrieve only this measurement annotation:
      [],
      // this is the initial depth of icicles:
      3,

      // aggregate at these levels in the tree:
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE, 4: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ],
    [
      'epiviz.data.EpivizApiDataProvider',
      'etec16s',
      'http://metaviz.cbcb.umd.edu/api',
      [],
      3,
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ],
    [
      'epiviz.data.EpivizApiDataProvider',
      'tbi_mouse',
      'http://metaviz.cbcb.umd.edu/api',
      [],
      3,
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ],
    [
      'epiviz.data.EpivizApiDataProvider',
      'hmp',
      'http://metaviz.cbcb.umd.edu/api',
      [],
      3,
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ],
    [
      'epiviz.data.EpivizApiDataProvider',
      'igs_test',
      'http://metaviz.cbcb.umd.edu/api',
      [],
      3,
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ]
];

// This sets up the UMD workspace server 
 epiviz.Config.SETTINGS.workspacesDataProvider = sprintf('epiviz.data.WebServerDataProvider,%s,%s',
     'workspaces_provider',
     'http://metaviz.cbcb.umd.edu/data/main.php');
>>>>>>> f2e6830fb168199513c9c7d094e236844b3cd924
