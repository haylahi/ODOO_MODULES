from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm

# class FormEmpresas(http.Controller):
#    @http.route('/demande-compte', auth="public", website=True)
#    def form_empresas(self, **kwargs):
#        return request.render('js_form_empresas_crm.js_form_empresas_crm_vista')

class WebsiteForm(WebsiteForm):
    @http.route('/demande-compte-societe/<string:model_name>', type='http', methods=['POST'], auth="public", website=True)
    def website_form(self, model_name, **kwargs):
        if model_name == 'crm.lead' and not request.params.get('state_id'):
            geoip_country_code = request.session.get('geoip', {}).get('country_code')
            geoip_state_code = request.session.get('geoip', {}).get('region')
            if geoip_country_code and geoip_state_code:
                State = request.env['res.country.state']
                request.params['state_id'] = State.search([('code', '=', geoip_state_code), ('country_id.code', '=', geoip_country_code)]).id

        return super(WebsiteForm, self).website_form(model_name, **kwargs)