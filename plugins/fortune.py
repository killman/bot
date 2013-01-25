from plugins.baseactionplugin import BaseActionPlugin
from ircmessage import IRCMessage
from ConfigParser import SafeConfigParser

import logging

class PluginFortunes(BaseActionPlugin):
  def __init__(self):
	## http://wertarbyte.de/gigaset-rss/
	self.base_url = """http://wertarbyte.de/gigaset-rss/?offensive=1&limit=140&cookies=1&lang=en&lang=es&format=rss&jar=de%2Fanekdoten%2Cde%2Fwusstensie%2Coff%2Flinux%2Coff%2Fmisogino.fortunes.u8%2Cde%2Fasciiart%2Cde%2Fzitate%2Coff%2Fmisandry%2Coff%2Fproverbios.fortunes.u8%2Cde%2Fbahnhof%2CMagic%208-Ball%2Coff%2Fmiscellaneous%2Coff%2Fvarios.fortunes.u8%2Cde%2Fbeilagen%2Cart%2Coff%2Fmisogyny%2Cpintadas.fortunes%2Cde%2Fbrot%2Cascii-art%2Coff%2Fpolitics%2Cpoder.fortunes%2Cde%2Fcomputer%2Cbofh-excuses%2Coff%2Fprivates%2Cproverbios.fortunes%2Cde%2Fdebian%2Ccomputers%2Coff%2Fracism%2Crefranes.fortunes%2Cde%2Fdessert%2Ccookie%2Coff%2Freligion%2Csabiduria.fortunes%2Cde%2Felefanten%2Cdebian%2Coff%2Friddles%2Cschopenhauer.fortunes%2Cde%2Fgedichte%2Cdebian-hints%2Coff%2Fsex%2Csentimientos.fortunes%2Cde%2Fhauptgericht%2Cdefinitions%2Coff%2Fsongs-poems%2Cvarios.fortunes%2Cde%2Fholenlassen%2Cdisclaimer%2Coff%2Fvulgarity%2Cvarios.fortunes-pre%2Cde%2Fhuhn%2Cdrugs%2Coff%2Fzippy%2Cverdad.fortunes%2Cde%2Finfodrom%2Ceducation%2Cparadoxum%2Cvida.fortunes%2Cde%2Fkalt%2Cethnic%2Cpeople%2Cfr%2FGDP%2Cde%2Fkinderzitate%2Cfood%2Cperl%2Cfr%2Fbd%2Cde%2Fkuchen%2Cfortunes%2Cpets%2Cfr%2Fcinema%2Cde%2Fletzteworte%2Cgoedel%2Cplatitudes%2Cfr%2Fdebian-fr%2Cde%2Flieberals%2Chumorists%2Cpolitics%2Cfr%2Fdroit%2Cde%2Flinuxtag%2Ckids%2Criddles%2Cfr%2Fgcu%2Cde%2Floewe%2Cknghtbrd%2Cscience%2Cfr%2Fgfa%2Cde%2Fmathematiker%2Claw%2Csongs-poems%2Cfr%2Fglp%2Cde%2Fms%2Clinux%2Csports%2Cfr%2Fgpj%2Cde%2Fmurphy%2Clinuxcookie%2Cstartrek%2Cfr%2Fhaiku%2Cde%2Fnamen%2Cliterature%2Ctranslate-me%2Cfr%2Fhumoristes%2Cde%2Fplaetzchen%2Clove%2Cwisdom%2Cfr%2Fhumour%2Cde%2Fquiz%2Cmagic%2Cwork%2Cfr%2Finformatique%2Cde%2Fregeln%2Cmedicine%2Czippy%2Cfr%2Flinuxfr-undernet%2Cde%2Fsalat%2Cmen-women%2Camistad.fortunes%2Cfr%2Flitterature_etrangere%2Cde%2Fsauce%2Cmiscellaneous%2Carte.fortunes%2Cfr%2Flitterature_francaise%2Cde%2Fsicherheitshinweise%2Cnews%2Casimov.fortunes%2Cfr%2Fmauriceetpatapon%2Cde%2Fsprichworte%2Coff%2Fart%2Cciencia.fortunes%2Cfr%2Fmultidesk%2Cde%2Fsprichwortev%2Coff%2Fastrology%2Cdeprimente.fortunes%2Cfr%2Fmultidesk2%2Cde%2Fsprueche%2Coff%2Fatheism%2Cfamilia.fortunes%2Cfr%2Fmysoginie%2Cde%2Fstilblueten%2Coff%2Fblack-humor%2Cfilosofia.fortunes%2Cfr%2Foulipo%2Cde%2Fsuppe%2Coff%2Fcookie%2Chumanos.fortunes%2Cfr%2Fpersonnalites%2Cde%2Ftips%2Coff%2Fdebian%2Cinformatica.fortunes%2Cfr%2Fphilosophie%2Cde%2Ftranslations%2Coff%2Fdefinitions%2Clao-tse.fortunes%2Cfr%2Fpolitique%2Cde%2Funfug%2Coff%2Fdrugs%2Cleydemurphy.fortunes%2Cfr%2Fproverbes%2Cde%2Fvornamen%2Coff%2Fethnic%2Clibertad.fortunes%2Cfr%2Freligion%2Cde%2Fvorspeise%2Coff%2Ffortunes%2Cnietzsche.fortunes%2Cfr%2Fsciences%2Cde%2Fwarmduscher%2Coff%2Fhphobia%2Coff%2Fcamioneros.fortunes.u8%2Cfr%2Ftolkien_fr%2Cde%2Fwitze%2Coff%2Fknghtbrd%2Coff%2Ffeministas.fortunes.u8%2Cfr%2Ftribune-linuxfr%2Cde%2Fwoerterbuch%2Coff%2Flimerick%2Coff%2Fmachosno.fortunes.u8"""
	
	#http://docs.python.org/2/library/xml.dom.minidom.html
	

  def execute(self, ircMsg, userRole):
    m = IRCMessage()
    m.user = ircMsg.user
    m.channel = ircMsg.channel

	
    #TODO: add localization
    m.msg = u"Listening to: {0} - {1}".format(last_track.title, last_track.artist.name)

    return m