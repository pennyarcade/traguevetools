<button
   id="compose"
   class="btn btn-sm btn-success btn-block"
   type="button"
   data-toggle="modal"
   data-target=".create-modal-lg"
>Create Issue</button>
% if not only_button:
    <div class="modal fade create-modal-lg" tabindex="-1" role="dialog" aria-hidden="true" style="display: none;">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form method="POST">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal">
                <span aria-hidden="true">×</span>
              </button>
              <h4 class="modal-title" id="myModalLabel">Create Issue</h4>
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