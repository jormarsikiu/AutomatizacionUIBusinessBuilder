from pytest_bdd import scenarios, given, when, then, parsers
from .objects import *
import time
from .login import *
import random

# Scenarios 
scenarios('../features/createbusinesspartner.feature')
PartnerCode = random.randint(0,1000)

@given('Abro el modulo business')
def abro_el_modulo_de_security(sb, login_con_cookies_usuario_y_contrasena):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/dashboard/security/index/MAP-001")
    sb.execute_script(Global.ButtonBusiness)
    time.sleep(1)

@given('presiono el boton business partner')
def presiono_el_boton_business_partenr(sb):  
    sb.execute_script(CreateBusinessPartner.ButtonBusinessPartner)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/BusinessPartner")
    time.sleep(3)

@when('presiono el boton de crear business partner')
def presiono_el_boton_crear_business_partenr(sb):  
    sb.execute_script(CreateBusinessPartner.ButtonBusinessPartnerCreate)
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/BusinessPartner/Form")
    time.sleep(3)

@when(parsers.parse('completo los datos del formulario de cliente {Name} {ShortName} {ComercialActivity} {TaxCode}'))
def completo_los_datos_de_formulario(sb,Name, ShortName,ComercialActivity, TaxCode):
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/BusinessPartner/Form")
    sb.execute_script(CreateBusinessPartner.SelectClientTypeOpen)
    sb.execute_script(CreateBusinessPartner.SelectClientType)
    sb.type("#PartnerCode", PartnerCode)
    sb.type("#PartnerName", Name)
    sb.type("#ShortName", ShortName)
    sb.type("#ComercialActivity", ComercialActivity)
    sb.type("#TaxCode", TaxCode)
    time.sleep(5)
    
@then('añado la Direccion Contabilidad Grupo Condicion comercial')
def anado_direccion_contabilidad_grupo_direccioncomercial(sb):  
    
    #Address
    sb.execute_script(CreateBusinessPartner.ButtonAddAddress)
    time.sleep(5)
    sb.execute_script(CreateBusinessPartner.ButtonOpenTypeAddress)
    time.sleep(3)
    sb.execute_script(CreateBusinessPartner.ButtonTypeAddress)
    time.sleep(3)
    sb.execute_script(CreateBusinessPartner.ButtonIsDelivery)
    sb.type("#pac-input", "Caracas")
    time.sleep(7)
   # sb.execute_script(CreateBusinessPartner.clickAddress2)
    #time.sleep(5)
    #sb.click("div.pac-item")
    sb.execute_script(Global.Accept)
    time.sleep(2)
    
    #Accounting
    sb.execute_script(CreateBusinessPartner.ButtonAccounting)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.ButtonAddAccounting)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectOpenAccounting)
    time.sleep(4)
    sb.execute_script(CreateBusinessPartner.SelectParentAccounting)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectOpenChildAccounting)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectChildAccounting)
    time.sleep(2)
    sb.execute_script(Global.Accept)
    time.sleep(2)
    
    #Groups
    sb.execute_script(CreateBusinessPartner.ButtonTapGroup)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.ButtonAddBPGroup)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectOpenGroup)
    time.sleep(4)
    sb.execute_script(CreateItem.SelectParentGroup)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectOpenChildGroup)
    time.sleep(2)
    sb.execute_script(CreateItem.SelectChildGroup)
    time.sleep(2)
    sb.execute_script(Global.Accept)
    time.sleep(2)
    
    #Business Condition
    sb.execute_script(CreateBusinessPartner.ButtonBussCond)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectOpenBussCond)
    time.sleep(4)
    sb.execute_script(CreateBusinessPartner.SelectBussCond)
    time.sleep(2)
    
    
@then('añado el Impuesto Atributos Equipos Contacto Imagen')
def anado_impuesto_atributos_equipos_contacto_imagen(sb): 
    #Tax
    sb.execute_script(CreateBusinessPartner.ButtonTax)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectOpenTax)
    time.sleep(7)
    sb.execute_script(CreateBusinessPartner.SelectTax)
    time.sleep(2)
    
    #Attributes
    sb.execute_script(CreateBusinessPartner.ButtonAttributes)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectOpenAttributes)
    time.sleep(4)
    sb.execute_script(CreateBusinessPartner.SelectAttributes)
    time.sleep(2)
    
    #Equipments
    sb.execute_script(CreateBusinessPartner.ButtonEquip)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.ButtonAddEquip)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectOpenEquip)
    time.sleep(4)
    sb.execute_script(CreateBusinessPartner.SelectEquip)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.InputEquip)
    time.sleep(2)
    sb.execute_script(Global.Accept)
    time.sleep(2)
    
    #Contact 
    sb.execute_script(CreateBusinessPartner.ButtonContact)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.ButtonAddContact)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.SelectOpenContact)
    time.sleep(4)
    sb.execute_script(CreateBusinessPartner.SelectContact)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.InputContact)
    time.sleep(2)
    sb.execute_script(Global.Accept)
    time.sleep(2)
    
    #Image
    sb.execute_script(CreateBusinessPartner.ButtonIamage)
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.ButtonAddImage)
    time.sleep(2)

    '''
    #Save
    #sb.execute_script(Global.SaveAll)
    #time.sleep(10)
    
    #Busqueda
    sb.is_valid_url("https://test-xweb.eurokaizen.com/Management/BusinessPartner")
    sb.execute_script(Global.Search)
    time.sleep(2)
    sb.execute_script(Global.FieldOpen)
    time.sleep(2)
    sb.execute_script(Global.FieldCode)
    time.sleep(2)
    sb.execute_script(Global.FieldOpenCondition)
    time.sleep(2)
    sb.execute_script(Global.FieldCondition)
    time.sleep(2)
    sb.type('[name*="Value"]', PartnerCode)
    time.sleep(2)
    sb.click("#btnSearchPanel")
    time.sleep(2)
    sb.execute_script(CreateBusinessPartner.EditIBP)
    time.sleep(8)
    '''