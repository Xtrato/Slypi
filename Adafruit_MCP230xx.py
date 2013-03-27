  


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py at master · adafruit/Adafruit-Raspberry-Pi-Python-Code · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="http://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="wLd0N4z1DcvM3yZ+PKRmgFv/zuBH9uS9KpiGJYDG0uk=" name="csrf-token" />

    <link href="https://a248.e.akamai.net/assets.github.com/assets/github-b3fe7e030b8a29c95b855b2d87adfee4e0ef3a28.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://a248.e.akamai.net/assets.github.com/assets/github2-988d2ea200531fd4663519e0bc2c1d050432a201.css" media="all" rel="stylesheet" type="text/css" />
    


      <script src="https://a248.e.akamai.net/assets.github.com/assets/frameworks-d76b58e749b52bc47a4c46620bf2c320fabe5248.js" type="text/javascript"></script>
      <script src="https://a248.e.akamai.net/assets.github.com/assets/github-847c6dd55da2c1941e239ce5737dd8d3b3535b05.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="ca70db712452429a1ce52e2662309641">

        <link data-pjax-transient rel='permalink' href='/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/3a876b2a6a4320048f093fd52b73bed214511065/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py'>
    <meta property="og:title" content="Adafruit-Raspberry-Pi-Python-Code"/>
    <meta property="og:type" content="githubog:gitrepository"/>
    <meta property="og:url" content="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code"/>
    <meta property="og:image" content="https://secure.gravatar.com/avatar/4bc2305bba6e4c82a64a8706ae8b3d40?s=420&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png"/>
    <meta property="og:site_name" content="GitHub"/>
    <meta property="og:description" content="Adafruit library code for Raspberry Pi. Contribute to Adafruit-Raspberry-Pi-Python-Code development by creating an account on GitHub."/>
    <meta property="twitter:card" content="summary"/>
    <meta property="twitter:site" content="@GitHub">
    <meta property="twitter:title" content="adafruit/Adafruit-Raspberry-Pi-Python-Code"/>

    <meta name="description" content="Adafruit library code for Raspberry Pi. Contribute to Adafruit-Raspberry-Pi-Python-Code development by creating an account on GitHub." />

  <link href="https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master.atom" rel="alternate" title="Recent Commits to Adafruit-Raspberry-Pi-Python-Code:master" type="application/atom+xml" />

  </head>


  <body class="logged_out page-blob  vis-public env-production  ">
    <div id="wrapper">

      

      
      
      

      
      <div class="header header-logged-out">
  <div class="container clearfix">

      <a class="header-logo-wordmark" href="https://github.com/">Github</a>

      <ul class="top-nav">
          <li class="explore"><a href="https://github.com/explore">Explore GitHub</a></li>
        <li class="search"><a href="https://github.com/search">Search</a></li>
        <li class="features"><a href="https://github.com/features">Features</a></li>
          <li class="blog"><a href="https://github.com/blog">Blog</a></li>
      </ul>

    <div class="header-actions">
        <a class="button primary" href="https://github.com/signup">Sign up for free</a>
      <a class="button" href="https://github.com/login?return_to=%2Fadafruit%2FAdafruit-Raspberry-Pi-Python-Code%2Fblob%2Fmaster%2FAdafruit_CharLCDPlate%2FAdafruit_MCP230xx.py">Sign in</a>
    </div>

  </div>
</div>


      

      


            <div class="site hfeed" itemscope itemtype="http://schema.org/WebPage">
      <div class="hentry">
        
        <div class="pagehead repohead instapaper_ignore readability-menu ">
          <div class="container">
            <div class="title-actions-bar">
              


<ul class="pagehead-actions">



    <li>
      <a href="/login?return_to=%2Fadafruit%2FAdafruit-Raspberry-Pi-Python-Code"
        class="minibutton js-toggler-target star-button entice tooltipped upwards"
        title="You must be signed in to use this feature" rel="nofollow">
        <span class="mini-icon mini-icon-star"></span>Star
      </a>
      <a class="social-count js-social-count" href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/stargazers">
        129
      </a>
    </li>
    <li>
      <a href="/login?return_to=%2Fadafruit%2FAdafruit-Raspberry-Pi-Python-Code"
        class="minibutton js-toggler-target fork-button entice tooltipped upwards"
        title="You must be signed in to fork a repository" rel="nofollow">
        <span class="mini-icon mini-icon-fork"></span>Fork
      </a>
      <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/network" class="social-count">
        70
      </a>
    </li>
</ul>

              <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
                <span class="repo-label"><span>public</span></span>
                <span class="mega-icon mega-icon-public-repo"></span>
                <span class="author vcard">
                  <a href="/adafruit" class="url fn" itemprop="url" rel="author">
                  <span itemprop="title">adafruit</span>
                  </a></span> /
                <strong><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="js-current-repository">Adafruit-Raspberry-Pi-Python-Code</a></strong>
              </h1>
            </div>

            
  <ul class="tabs">
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="selected" highlight="repo_source repo_downloads repo_commits repo_tags repo_branches">Code</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/network" highlight="repo_network">Network</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/pulls" highlight="repo_pulls">Pull Requests <span class='counter'>0</span></a></li>

      <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/issues" highlight="repo_issues">Issues <span class='counter'>2</span></a></li>



    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/graphs" highlight="repo_graphs repo_contributors">Graphs</a></li>


  </ul>
  
<div class="tabnav">

  <span class="tabnav-right">
    <ul class="tabnav-tabs">
          <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/tags" class="tabnav-tab" highlight="repo_tags">Tags <span class="counter blank">0</span></a></li>
    </ul>
    
  </span>

  <div class="tabnav-widget scope">


    <div class="select-menu js-menu-container js-select-menu js-branch-menu">
      <a class="minibutton select-menu-button js-menu-target" data-hotkey="w" data-ref="master">
        <span class="mini-icon mini-icon-branch"></span>
        <i>branch:</i>
        <span class="js-select-button">master</span>
      </a>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">

        <div class="select-menu-modal">
          <div class="select-menu-header">
            <span class="select-menu-title">Switch branches/tags</span>
            <span class="mini-icon mini-icon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-filters">
            <div class="select-menu-text-filter">
              <input type="text" id="commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
            </div>
            <div class="select-menu-tabs">
              <ul>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
                </li>
                <li class="select-menu-tab">
                  <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
                </li>
              </ul>
            </div><!-- /.select-menu-tabs -->
          </div><!-- /.select-menu-filters -->

          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="branches">

            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

                <div class="select-menu-item js-navigation-item js-navigation-target selected">
                  <span class="select-menu-item-icon mini-icon mini-icon-confirm"></span>
                  <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/master/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py" class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target" data-name="master" rel="nofollow" title="master">master</a>
                </div> <!-- /.select-menu-item -->
            </div>

              <div class="select-menu-no-results">Nothing to show</div>
          </div> <!-- /.select-menu-list -->


          <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket css-truncate" data-tab-filter="tags">
            <div data-filterable-for="commitish-filter-field" data-filterable-type="substring">

            </div>

            <div class="select-menu-no-results">Nothing to show</div>

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

  </div> <!-- /.scope -->

  <ul class="tabnav-tabs">
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="selected tabnav-tab" highlight="repo_source">Files</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master" class="tabnav-tab" highlight="repo_commits">Commits</a></li>
    <li><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/branches" class="tabnav-tab" highlight="repo_branches" rel="nofollow">Branches <span class="counter ">1</span></a></li>
  </ul>

</div>

  
  
  


            
          </div>
        </div><!-- /.repohead -->

        <div id="js-repo-pjax-container" class="container context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:f6cd0e89cfaa84f9b95b2517c07ad8a1 -->
<!-- blob contrib frag key: views10/v8/blob_contributors:v21:f6cd0e89cfaa84f9b95b2517c07ad8a1 -->


<div id="slider">
    <div class="frame-meta">

      <p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

        <div class="breadcrumb">
          <span class='bold'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">Adafruit-Raspberry-Pi-Python-Code</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_CharLCDPlate" class="js-slide-to" data-branch="master" data-direction="back" itemscope="url"><span itemprop="title">Adafruit_CharLCDPlate</span></a></span><span class="separator"> / </span><strong class="final-path">Adafruit_MCP230xx.py</strong> <span class="js-zeroclipboard zeroclipboard-button" data-clipboard-text="Adafruit_CharLCDPlate/Adafruit_MCP230xx.py" data-copied-hint="copied!" title="copy to clipboard"><span class="mini-icon mini-icon-clipboard"></span></span>
        </div>

      <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/find/master" class="js-slide-to" data-hotkey="t" style="display:none">Show File Finder</a>


        
  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://secure.gravatar.com/avatar/8d326e1c43b0e5988564f7bf512e28a5?s=140&amp;d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png" width="24" />
    <span class="author"><span rel="author">root</span></span>
    <time class="js-relative-date" datetime="2012-11-19T14:03:38-08:00" title="2012-11-19 14:03:38">November 19, 2012</time>
    <div class="commit-title">
        <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commit/cc3fefcda0fc80dbde3207fa6a9c809c045995f7" class="message">yay lcd plate</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>0</strong> contributors</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2>Users on GitHub who have contributed to this file</h2>
      <ul class="facebox-user-list">
      </ul>
    </div>
  </div>


    </div><!-- ./.frame-meta -->

    <div class="frames">
      <div class="frame" data-permalink-url="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blob/3a876b2a6a4320048f093fd52b73bed214511065/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py" data-title="Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py at master · adafruit/Adafruit-Raspberry-Pi-Python-Code · GitHub" data-type="blob">

        <div id="files" class="bubble">
          <div class="file">
            <div class="meta">
              <div class="info">
                <span class="icon"><b class="mini-icon mini-icon-text-file"></b></span>
                <span class="mode" title="File Mode">symbolic link</span>
                  <span>1 lines (1 sloc)</span>
                <span>0.078 kb</span>
              </div>
              <div class="actions">
                <div class="button-group">
                      <a class="minibutton js-entice" href=""
                         data-entice="You must be signed in and on a branch to make or propose changes">Edit</a>
                  <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/raw/master/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py" class="button minibutton " id="raw-url">Raw</a>
                    <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/blame/master/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py" class="button minibutton ">Blame</a>
                  <a href="/adafruit/Adafruit-Raspberry-Pi-Python-Code/commits/master/Adafruit_CharLCDPlate/Adafruit_MCP230xx.py" class="button minibutton " rel="nofollow">History</a>
                </div><!-- /.button-group -->
              </div><!-- /.actions -->

            </div>
                <div class="data type-python js-blob-data">
      <table cellpadding="0" cellspacing="0" class="lines">
        <tr>
          <td>
            <pre class="line_numbers"><span id="L1" rel="#L1">1</span>
</pre>
          </td>
          <td width="100%">
                  <div class="highlight"><pre><div class='line' id='LC1'><span class="o">../../</span><span class="n">Adafruit</span><span class="o">-</span><span class="n">Raspberry</span><span class="o">-</span><span class="n">Pi</span><span class="o">-</span><span class="n">Python</span><span class="o">-</span><span class="n">Code</span><span class="o">/</span><span class="n">Adafruit_MCP230xx</span><span class="o">/</span><span class="n">Adafruit_MCP230xx</span><span class="o">.</span><span class="n">py</span></div></pre></div>
          </td>
        </tr>
      </table>
  </div>

          </div>
        </div>

        <a href="#jump-to-line" rel="facebox" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
        <div id="jump-to-line" style="display:none">
          <h2>Jump to Line</h2>
          <form accept-charset="UTF-8" class="js-jump-to-line-form">
            <input class="textfield js-jump-to-line-field" type="text">
            <div class="full-button">
              <button type="submit" class="button">Go</button>
            </div>
          </form>
        </div>

      </div>
    </div>
</div>

<div id="js-frame-loading-template" class="frame frame-loading large-loading-area" style="display:none;">
  <img class="js-frame-loading-spinner" src="https://a248.e.akamai.net/assets.github.com/images/spinners/octocat-spinner-128.gif?1360648847" height="64" width="64">
</div>


        </div>
      </div>
      <div class="context-overlay"></div>
    </div>

      <div id="footer-push"></div><!-- hack for sticky footer -->
    </div><!-- end of wrapper - hack for sticky footer -->

      <!-- footer -->
      <div id="footer">
  <div class="container clearfix">

      <dl class="footer_nav">
        <dt>GitHub</dt>
        <dd><a href="https://github.com/about">About us</a></dd>
        <dd><a href="https://github.com/blog">Blog</a></dd>
        <dd><a href="https://github.com/contact">Contact &amp; support</a></dd>
        <dd><a href="http://enterprise.github.com/">GitHub Enterprise</a></dd>
        <dd><a href="http://status.github.com/">Site status</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Applications</dt>
        <dd><a href="http://mac.github.com/">GitHub for Mac</a></dd>
        <dd><a href="http://windows.github.com/">GitHub for Windows</a></dd>
        <dd><a href="http://eclipse.github.com/">GitHub for Eclipse</a></dd>
        <dd><a href="http://mobile.github.com/">GitHub mobile apps</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Services</dt>
        <dd><a href="http://get.gaug.es/">Gauges: Web analytics</a></dd>
        <dd><a href="http://speakerdeck.com">Speaker Deck: Presentations</a></dd>
        <dd><a href="https://gist.github.com">Gist: Code snippets</a></dd>
        <dd><a href="http://jobs.github.com/">Job board</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>Documentation</dt>
        <dd><a href="http://help.github.com/">GitHub Help</a></dd>
        <dd><a href="http://developer.github.com/">Developer API</a></dd>
        <dd><a href="http://github.github.com/github-flavored-markdown/">GitHub Flavored Markdown</a></dd>
        <dd><a href="http://pages.github.com/">GitHub Pages</a></dd>
      </dl>

      <dl class="footer_nav">
        <dt>More</dt>
        <dd><a href="http://training.github.com/">Training</a></dd>
        <dd><a href="https://github.com/edu">Students &amp; teachers</a></dd>
        <dd><a href="http://shop.github.com">The Shop</a></dd>
        <dd><a href="/plans">Plans &amp; pricing</a></dd>
        <dd><a href="http://octodex.github.com/">The Octodex</a></dd>
      </dl>

      <hr class="footer-divider">


    <p class="right">&copy; 2013 <span title="0.04735s from fe4.rs.github.com">GitHub</span>, Inc. All rights reserved.</p>
    <a class="left" href="https://github.com/">
      <span class="mega-icon mega-icon-invertocat"></span>
    </a>
    <ul id="legal">
        <li><a href="https://github.com/site/terms">Terms of Service</a></li>
        <li><a href="https://github.com/site/privacy">Privacy</a></li>
        <li><a href="https://github.com/security">Security</a></li>
    </ul>

  </div><!-- /.container -->

</div><!-- /.#footer -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/adafruit/Adafruit-Raspberry-Pi-Python-Code/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-icon mega-icon-normalscreen"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="mini-icon mini-icon-brightness"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="mini-icon mini-icon-exclamation"></span>
      Something went wrong with that request. Please try again.
      <a href="#" class="mini-icon mini-icon-remove-close ajax-error-dismiss"></a>
    </div>

    
    
    <span id='server_response_time' data-time='0.04795' data-host='fe4'></span>
    
  </body>
</html>

