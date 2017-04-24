<ul class="list-unstyled msg_list">
    % if issue.has_key('comments'):
      % for comment in issue['comments']:
        <li>
          <a>
            <span class="image">
              <img src="{{comment['author_info']['avatar']}}" alt="[img]">
            </span>&nbsp;
            <span>
              <span>{{comment['author_info']['display_name']}}</span>
              <span class="time">{{comment['utc_created_on'].strftime('%y-%m-%d %H:%M')}}&nbsp;&nbsp;</span>
            </span>
            <span class="message">{{comment['content']}}</span>
          </a>
        </li>
      % end
    % end
</ul>