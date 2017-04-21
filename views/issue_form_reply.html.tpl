
<button
  class="btn btn-sm btn-primary"
  type="button"
  data-toggle="modal"
  data-target=".reply-modal-lg"
>
    <i class="fa fa-reply"></i> Reply
</button>
% if not only_button:
    <div class="modal fade reply-modal-lg" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form method="POST">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">
                <span aria-hidden="true">×</span>
              </button>
              <h4 class="modal-title" id="myModalLabel">Reply to issue</h4>
            </div>
            <div class="modal-body">
              -- place form here --
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary">Save changes</button>
            </div>
          </form>
        </div>
      </div>
    </div>
% end