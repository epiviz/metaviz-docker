// This uses the UMD server for login and user management
epiviz.Config.SETTINGS.dataServerLocation = 'http://metaviz.cbcb.umd.edu/data/';

epiviz.Config.SETTINGS.dataProviders = [
    [
      // fully qualified class name for the class
      'epiviz.data.EpivizApiDataProvider',

      // the name of the datasource (matching the datasource in the UI add measurements dialog)
      'msd16s',

      // where the api is located, relative to dataServerLocation (see above)
      //'hmp-api/',
      'api/',
      //'http://metaviz.cbcb.umd.edu:5000/api',

      // retrieve only this measurement annotation:
      //['sex', 'hmpbodysubsite', 'hmpbodysupersite', 'sampcollectdevice', 'envmatter', 'bodysite', 'bmi', 'visitno', 'age', 'runcenter', 'runid', 'description'],

      [],
      // this is the initial depth of icicles:
      3,

      // aggregate at these levels in the tree:
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE, 4: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ],
    [
      'epiviz.data.EpivizApiDataProvider',
      'etec16s',
      'api/',
      [],
      3,
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ],
    [
      'epiviz.data.EpivizApiDataProvider',
      'tbi_mouse',
      'api/',
      [],
      3,
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ],
    [
      'epiviz.data.EpivizApiDataProvider',
      'hmp',
      'api/',
      [],
      3,
      {3: epiviz.ui.charts.tree.NodeSelectionType.NODE}
    ]
];


// This sets up the UMD workspace server 
epiviz.Config.SETTINGS.workspacesDataProvider = sprintf('epiviz.data.WebServerDataProvider,%s,%s',
    'workspaces_provider',
    'http://metaviz.cbcb.umd.edu/data/main.php');
