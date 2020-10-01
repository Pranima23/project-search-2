from django.shortcuts import render, redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
            return redirect(f'/login?return_url={returnUrl}')
            #return redirect('login')
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware