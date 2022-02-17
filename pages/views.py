# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.http.response import Http404
# from django.shortcuts import redirect
# import os


# class StaticRouteView(TemplateView):
#     def render_to_response(self, context, **response_kwargs):
#         path = self.kwargs.get("route")
#         try:
#             return super().render_to_response(context, **response_kwargs)
#         except:
#             if os.path.exists(path + "/"):
#                 return redirect(path + "/")
#             raise Http404()

#     def get_template_names(self):
#         try:
#             path = self.kwargs.get("route")
#             if path[-1] == "/":
#                 path = path[:-1]
#             if path[0] == "/":
#                 path = path[1:]

#             return [path]
#         except Exception as e:
#             raise Http404()
